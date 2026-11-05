import json
import re
import sys

KEYS = ("comments", "brackets", "autoClosingPairs", "surroundingPairs")


def strip_jsonc(text):
    out = []
    i = 0
    in_string = False
    while i < len(text):
        ch = text[i]
        if in_string:
            out.append(ch)
            if ch == "\\":
                out.append(text[i + 1])
                i += 2
                continue
            if ch == '"':
                in_string = False
            i += 1
        elif ch == '"':
            in_string = True
            out.append(ch)
            i += 1
        elif text.startswith("//", i):
            i = text.find("\n", i)
            i = len(text) if i < 0 else i
        elif text.startswith("/*", i):
            i = text.index("*/", i) + 2
        else:
            out.append(ch)
            i += 1
    return re.sub(r",(\s*[}\]])", r"\1", "".join(out))


def as_pair(item):
    if isinstance(item, list):
        return {"open": item[0], "close": item[1]}
    return {"open": item["open"], "close": item["close"]}


def convert(path):
    with open(path, encoding="utf-8") as f:
        raw = json.loads(strip_jsonc(f.read()))
    config = {key: raw[key] for key in KEYS if key in raw}
    for key in ("autoClosingPairs", "surroundingPairs"):
        if key in config:
            config[key] = [as_pair(item) for item in config[key]]
    block = config.get("comments", {}).get("blockComment")
    if block and "brackets" in config:
        config["brackets"] = [pair for pair in config["brackets"] if list(pair) != list(block)]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write("\n")


for path in sys.argv[1:]:
    convert(path)
    print(f"converted {path}")
