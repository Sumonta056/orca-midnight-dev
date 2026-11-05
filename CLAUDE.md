# Midnight Dev with Rich Syntax

An Orca plugin (`execution: "data"`, nothing runs): a Monokai-style app theme, a terminal theme and TextMate grammars for Java, Vue, Go, Python, C and C++. Colors derive from Bearded Theme Monokai Reversed. Published at github.com/Sumonta056/orca-midnight-dev; the community catalog lists it from the `orca-plugin` topic and each `v*` tag.

## Invariants

- The plugin id and both theme ids stay `monokai-midnight`. The catalog key `sumonta056.monokai-midnight` and users' saved theme settings depend on them; the display name can change freely.
- A pushed tag is permanent. The catalog refuses a moved tag, so every change ships as a new version.
- Commits go on a branch (`release/vX.Y.Z` or `chore/...`). A hook blocks commits on `main`; the user merges, pushes and tags.
- Every color reaches Orca through one of 24 token types. Before you judge a color, ask which type the token lands on.

## Check

```sh
python3 -I scripts/check-theme.py
orca plugin validate .
orca plugin dev reload "$PWD"
orca plugin list
```

A change is done when both checks pass and `orca plugin list` shows `local.monokai-midnight … idle`. Orca reloads this folder by itself only while it is a development folder (`data, dev` in the list); `orca plugin dev load "$PWD"` makes it one. Colors are confirmed only in a screenshot from the user, because the agent cannot see the Orca window.

`Test/` holds sample files for that screenshot. It is in `.gitignore`.

## Rules

- Editing `themes/` or `terminal/`, or judging a code color: read `.claude/rules/theme.md`.
- Editing `syntaxes/` or `scripts/`, or a file type colored wrongly: read `.claude/rules/grammars.md`.
- Changing `orca-plugin.json` or preparing a release: read `.claude/rules/release.md`.
