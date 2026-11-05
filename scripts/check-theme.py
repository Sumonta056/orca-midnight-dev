import json
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MAX_BYTES = 16 * 1024

TOKENS = {
    "--background", "--editor-surface", "--foreground", "--card", "--card-foreground", "--popover",
    "--popover-foreground", "--primary", "--primary-foreground", "--secondary", "--secondary-foreground",
    "--muted", "--muted-foreground", "--accent", "--accent-foreground", "--border", "--input", "--ring",
    "--chart-1", "--chart-2", "--chart-3", "--chart-4", "--chart-5", "--sidebar", "--sidebar-foreground",
    "--sidebar-primary", "--sidebar-primary-foreground", "--sidebar-accent", "--sidebar-accent-foreground",
    "--sidebar-border", "--sidebar-ring", "--worktree-sidebar", "--worktree-sidebar-foreground",
    "--worktree-sidebar-accent", "--worktree-sidebar-accent-foreground", "--worktree-sidebar-border",
    "--worktree-sidebar-ring", "--worktree-sidebar-active", "--worktree-sidebar-active-border", "--host-badge",
    "--host-badge-foreground", "--tab-bar", "--tab-active", "--tab-active-foreground", "--tab-active-indicator",
    "--tab-inactive", "--tab-inactive-foreground", "--split-divider", "--split-divider-hover",
    "--chat-user-message", "--text-link", "--diff-added", "--diff-removed", "--git-decoration-added",
    "--git-decoration-modified", "--git-decoration-deleted", "--git-decoration-renamed",
    "--git-decoration-untracked", "--git-decoration-copied", "--git-decoration-ignored",
}
TEXT_PAIRS = [
    ("--background", "--foreground"), ("--background", "--muted-foreground"),
    ("--editor-surface", "--foreground"), ("--editor-surface", "--muted-foreground"),
    ("--card", "--card-foreground"), ("--popover", "--popover-foreground"),
    ("--primary", "--primary-foreground"), ("--secondary", "--secondary-foreground"),
    ("--muted", "--muted-foreground"), ("--accent", "--accent-foreground"),
    ("--sidebar", "--sidebar-foreground"), ("--sidebar-primary", "--sidebar-primary-foreground"),
    ("--sidebar-accent", "--sidebar-accent-foreground"), ("--worktree-sidebar", "--worktree-sidebar-foreground"),
    ("--worktree-sidebar-accent", "--worktree-sidebar-accent-foreground"),
    ("--tab-active", "--tab-active-foreground"), ("--tab-inactive", "--tab-inactive-foreground"),
    ("--host-badge", "--host-badge-foreground"), ("--worktree-sidebar-active", "--worktree-sidebar-foreground"),
    ("--chat-user-message", "--foreground"), ("--editor-surface", "--text-link"),
]
RINGS = [("--ring", "--background"), ("--sidebar-ring", "--sidebar"), ("--worktree-sidebar-ring", "--worktree-sidebar")]
BORDERS = ["--border", "--input", "--sidebar-border", "--worktree-sidebar-border"]
MONACO_DARK_DEFAULTS = ["#608b4e", "#ce9178", "#569cd6", "#3dc9b0", "#b5cea8"]
TERMINAL_KEYS = {
    "foreground", "background", "cursor", "cursorAccent", "selectionBackground", "selectionForeground",
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "brightBlack", "brightRed",
    "brightGreen", "brightYellow", "brightBlue", "brightMagenta", "brightCyan", "brightWhite",
}
FONT_STYLE = re.compile(r"^(?:(?:italic|bold|underline|strikethrough)(?: (?:italic|bold|underline|strikethrough))*)?$")

failures = []


def check(ok, message):
    if not ok:
        failures.append(message)


def read(relative):
    with open(os.path.join(ROOT, relative), encoding="utf-8") as f:
        return json.load(f)


def probe(value):
    match = re.fullmatch(r"#([0-9a-fA-F]{6})([0-9a-fA-F]{2})?", value or "")
    if not match:
        return None
    rgb = [int(match[1][i:i + 2], 16) for i in (0, 2, 4)]
    return rgb + [int(match[2], 16) / 255 if match[2] else 1]


def luminance(color):
    def channel(v):
        c = v / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * channel(color[0]) + 0.7152 * channel(color[1]) + 0.0722 * channel(color[2])


def contrast(a, b):
    high, low = sorted([luminance(a), luminance(b)], reverse=True)
    return (high + 0.05) / (low + 0.05)


manifest = read("orca-plugin.json")

for entry in manifest["contributes"]["themes"]:
    name = entry["id"]
    size = os.path.getsize(os.path.join(ROOT, entry["path"]))
    check(size <= MAX_BYTES, f"{name}: {size} bytes, over the {MAX_BYTES}-byte limit")
    theme = read(entry["path"])
    check(theme.get("base") in ("light", "dark"), f"{name}: base must be light or dark")
    check(set(theme) <= {"schemaVersion", "base", "tokens", "tokenColors"}, f"{name}: unknown top-level key")
    colors = {}
    for token, value in theme["tokens"].items():
        check(token in TOKENS, f"{name}: {token} is not a public token")
        colors[token] = probe(value)
        check(colors[token] is not None, f"{name}: {token} {value} is not a hex color")
    lowest_text = 99
    for surface, text in TEXT_PAIRS:
        if surface not in colors or text not in colors:
            continue
        check(colors[surface][3] == 1 and colors[text][3] == 1, f"{name}: {surface}/{text} must be opaque")
        ratio = contrast(colors[surface], colors[text])
        lowest_text = min(lowest_text, ratio)
        check(ratio >= 4.5, f"{name}: {text} on {surface} is {ratio:.2f}:1, needs 4.5")
    for ring, surface in RINGS:
        ratio = contrast(colors[ring], colors[surface])
        check(ratio >= 2, f"{name}: {ring} on {surface} is {ratio:.2f}:1, needs 2")
    for border in BORDERS:
        check(colors[border][3] >= 0.05, f"{name}: {border} alpha below 0.05")
    for token in (t for t in colors if t.startswith("--git-decoration-")):
        ratio = contrast(colors[token], colors["--sidebar"])
        check(ratio >= 3, f"{name}: {token} on --sidebar is {ratio:.2f}:1, needs 3")
    editor = colors["--editor-surface"]
    for default in MONACO_DARK_DEFAULTS:
        check(contrast(probe(default), editor) >= 3, f"{name}: Monaco default {default} under 3:1, Orca would skip the editor theme")
    lowest_code = 99
    for rule in theme["tokenColors"]:
        scopes = rule["scope"] if isinstance(rule["scope"], list) else [rule["scope"]]
        label = scopes[0]
        for scope in scopes:
            check(not re.search(r"[\s,]", scope), f"{name}: scope '{scope}' is a selector Orca skips")
        check(set(rule["settings"]) <= {"foreground", "fontStyle"}, f"{name}: '{label}' has an unknown setting")
        if "fontStyle" in rule["settings"]:
            check(FONT_STYLE.match(rule["settings"]["fontStyle"]) is not None, f"{name}: '{label}' bad fontStyle")
        if "foreground" in rule["settings"]:
            color = probe(rule["settings"]["foreground"])
            check(color is not None and color[3] == 1, f"{name}: '{label}' foreground must be opaque hex")
            if color:
                ratio = contrast(color, editor)
                lowest_code = min(lowest_code, ratio)
                check(ratio >= 3, f"{name}: '{label}' {rule['settings']['foreground']} is {ratio:.2f}:1, Orca drops code colors under 3")
    print(f"{name}: {size} bytes, {len(theme['tokens'])} tokens, {len(theme['tokenColors'])} code rules, "
          f"lowest text {lowest_text:.2f}:1, lowest code {lowest_code:.2f}:1")

for entry in manifest["contributes"].get("terminalThemes", []):
    name = entry["id"]
    theme = read(entry["path"])
    terminal = theme["terminal"]
    check(theme.get("schemaVersion") == 1, f"{name} terminal: schemaVersion must be 1")
    check(theme.get("mode") in ("dark", "light", "unknown"), f"{name} terminal: bad mode")
    for key, value in terminal.items():
        check(key in TERMINAL_KEYS, f"{name} terminal: unknown key {key}")
        check(re.fullmatch(r"#[0-9a-fA-F]{6}", value) is not None, f"{name} terminal: {key} {value} is not #rrggbb")
    ratio = contrast(probe(terminal["foreground"]), probe(terminal["background"]))
    print(f"{name} terminal: {len(terminal)} colors, text {ratio:.2f}:1")

if failures:
    print("\n" + "\n".join(failures))
    sys.exit(1)
print("All themes pass.")
