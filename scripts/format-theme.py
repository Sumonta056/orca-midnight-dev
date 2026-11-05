import json
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "themes", "monokai-midnight.json")


def compact(value):
    return json.dumps(value, separators=(", ", ": "), ensure_ascii=False)


with open(PATH, encoding="utf-8") as f:
    theme = json.load(f)

lines = ["{", f'  "base": {compact(theme["base"])},', '  "tokens": {']
tokens = list(theme["tokens"].items())
for index, (token, value) in enumerate(tokens):
    lines.append(f"    {compact(token)}: {compact(value)}" + ("," if index < len(tokens) - 1 else ""))
lines += ["  },", '  "tokenColors": [']
rules = theme["tokenColors"]
for index, rule in enumerate(rules):
    entry = {"scope": rule["scope"], "settings": rule["settings"]}
    lines.append(f"    {compact(entry)}" + ("," if index < len(rules) - 1 else ""))
lines += ["  ]", "}"]
text = "\n".join(lines) + "\n"

if json.loads(text) != {"base": theme["base"], "tokens": theme["tokens"], "tokenColors": [{"scope": r["scope"], "settings": r["settings"]} for r in rules]}:
    sys.exit("format-theme: formatted output does not match the input")
with open(PATH, "w", encoding="utf-8") as f:
    f.write(text)
print(f"{PATH}: {len(text.encode())} bytes")
