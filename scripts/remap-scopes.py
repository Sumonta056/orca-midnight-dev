import json
import re
import sys
from collections import Counter

RULES = [
    (re.compile(r"^storage\.type(?P<rest>(?:\.generic(?:\.wildcard)?|\.object\.array|\.primitive(?:\.array)?|\.annotation)?)\.java$"),
     r"support.type\g<rest>.java"),
    (re.compile(r"^storage\.type\.(?P<kind>boolean|byte|error|numeric|rune|string|uintptr)\.go$"),
     r"support.type.\g<kind>.go"),
    (re.compile(r"^storage\.type\.(?P<kind>built-in(?:\.primitive)?|primitive)\.(?P<lang>c|cpp)$"),
     r"support.type.\g<kind>.\g<lang>"),
    (re.compile(r"^constant\.language(?P<rest>(?:\.[\w-]+)*)$"),
     r"constant.other.language\g<rest>"),
    (re.compile(r"^entity\.name\.function\.decorator\.python$"),
     "entity.name.decorator.python"),
    (re.compile(r"^storage\.modifier\.(?P<kind>import|package)\.java$"),
     r"meta.path.\g<kind>.java"),
    (re.compile(r"^variable\.other\.(?P<kind>object(?:\.property)?|property)\.(?P<lang>java|ts|js)$"),
     r"support.variable.\g<kind>.\g<lang>"),
    (re.compile(r"^variable\.language\.(?P<kind>this|super)\.(?P<lang>java|ts|js)$"),
     r"support.variable.language.\g<kind>.\g<lang>"),
    (re.compile(r"^support\.type\.property-name\.css$"),
     "variable.other.property-name.css"),
    (re.compile(r"^entity\.name\.tag\.html\.vue$"),
     "support.class.component.html.vue"),
    (re.compile(r"^punctuation\.definition\.string\.(?P<edge>begin|end)\.html\.vue$"),
     r"string.quoted.\g<edge>.html.vue"),
    (re.compile(r"^(?P<scope>storage\.type\.(?:class|enum|function|interface|property|type)|keyword\.other(?:\.debugger)?)\.(?P<lang>ts|js)$"),
     r"string.regexp.\g<scope>.\g<lang>"),
    (re.compile(r"^keyword\.other\.package\.java$"),
     "string.regexp.keyword.other.package.java"),
]


def rename(value, counts):
    parts = []
    for part in value.split(" "):
        for pattern, replacement in RULES:
            if pattern.match(part):
                new = pattern.sub(replacement, part)
                counts[f"{part} -> {new}"] += 1
                part = new
                break
        parts.append(part)
    return " ".join(parts)


def walk(node, counts):
    if isinstance(node, dict):
        for key, value in node.items():
            if key in ("name", "contentName") and isinstance(value, str):
                node[key] = rename(value, counts)
            else:
                walk(value, counts)
    elif isinstance(node, list):
        for item in node:
            walk(item, counts)


for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as f:
        grammar = json.load(f)
    counts = Counter()
    walk(grammar, counts)
    if counts:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(grammar, f, indent="\t", ensure_ascii=False)
            f.write("\n")
        print(f"{path}: {sum(counts.values())} renames")
        for change, n in sorted(counts.items()):
            print(f"  {n:3}  {change}")
