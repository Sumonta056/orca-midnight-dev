import json
import sys

INTERPOLATIONS = {"include": "text.html.vue#vue-interpolations"}
DIRECTIVES = {"include": "text.html.vue#vue-directives"}
CLASS_LIST = {
    "match": "(?<![\\w:@.#-])(class)\\s*(=)\\s*(?:(\")([^\"]*)(\")|(')([^']*)('))",
    "name": "meta.attribute.class.html",
    "captures": {
        "1": {"name": "entity.other.attribute-name.html"},
        "2": {"name": "punctuation.separator.key-value.html"},
        "3": {"name": "string.quoted.double.html"},
        "4": {"name": "string.regexp.class-list.html"},
        "5": {"name": "string.quoted.double.html"},
        "6": {"name": "string.quoted.single.html"},
        "7": {"name": "string.regexp.class-list.html"},
        "8": {"name": "string.quoted.single.html"},
    },
}

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    grammar = json.load(f)

if grammar.get("scopeName") != "text.html.basic":
    sys.exit(f"{path}: expected scope text.html.basic, got {grammar.get('scopeName')}")
attribute = grammar["repository"]["attribute"]["patterns"]

if INTERPOLATIONS not in grammar["patterns"]:
    grammar["patterns"].insert(0, INTERPOLATIONS)
if CLASS_LIST not in attribute:
    attribute.insert(0, CLASS_LIST)
if DIRECTIVES not in attribute:
    attribute.insert(0, DIRECTIVES)

with open(path, "w", encoding="utf-8") as f:
    json.dump(grammar, f, indent="\t", ensure_ascii=False)
    f.write("\n")
print(f"{path}: added Vue interpolations and directives")
