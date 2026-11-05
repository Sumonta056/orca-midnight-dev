import json
import sys


def prune(node, repository, dropped):
    if isinstance(node, dict):
        return {key: prune(value, repository, dropped) for key, value in node.items()}
    if isinstance(node, list):
        kept = []
        for item in node:
            include = item.get("include") if isinstance(item, dict) else None
            if isinstance(include, str) and include.startswith("#") and include[1:] not in repository:
                dropped.append(include)
                continue
            kept.append(prune(item, repository, dropped))
        return kept
    return node


for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as f:
        grammar = json.load(f)
    dropped = []
    fixed = prune(grammar, set(grammar.get("repository", {})), dropped)
    if dropped:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(fixed, f, indent="\t", ensure_ascii=False)
            f.write("\n")
        print(f"{path}: dropped {len(dropped)} broken include(s): {sorted(set(dropped))}")
