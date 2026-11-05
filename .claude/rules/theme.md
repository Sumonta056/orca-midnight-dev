---
paths:
  - "themes/**"
  - "terminal/**"
---

# Theme colors

## How Orca turns a token into a color

1. A tokenizer gives each word a scope. Grammar files in `syntaxes/` give full TextMate scopes; Orca's built-in tokenizers (all `.ts`, `.js`, `.json`, `.css`, `.html`, `.md` files) give coarse Monaco names such as `keyword` and `identifier`.
2. Orca reduces the scope to one of 24 token types (`plugin-syntax-token-legend.ts` in stablyai/orca).
3. Orca colors each type with exactly one theme scope (`plugin-monaco-token-rules.ts`): the longest `tokenColors` selector that is a dot-prefix of that scope.

So the theme sets about 24 colors, and only the rules for these lookup scopes reach the Orca editor:

| Token type | Lookup scope | Color |
| --- | --- | --- |
| keyword | `keyword` | yellow `#ffd866` |
| keyword.flow | `keyword.control` | yellow |
| operator | `keyword.operator` | yellow |
| identifier | `variable` | text `#c6cad7` |
| type | `entity.name.type` | purple `#ab9df2` |
| function | `entity.name.function` | blue `#78dce8` |
| variable.predefined | `support.variable` | orange `#fc9867` |
| variable.parameter | `variable.parameter` | pink `#e991e3` |
| annotation | `meta.decorator` | pink |
| string, attribute.value | `string` | green `#a9dc76` |
| regexp | `string.regexp` | turquoise `#78e8c6` |
| number | `constant.numeric` | orange |
| constant | `constant` | red `#fc6a67` |
| comment | `comment` | slate italic `#5a617a` |
| delimiter | `punctuation` | gray `#5f626b` |
| tag | `entity.name.tag` | blue |
| attribute.name | `entity.other.attribute-name` | yellow |

The other `tokenColors` rules are Bearded's VS Code rules; keep them, because they document the intended colors and the grammar renames rely on the same palette. Bracket pairs get Orca's rainbow bracket colors, not theme colors.

## Limits Orca enforces

- The theme file is at most 16,384 bytes. `scripts/format-theme.py` writes one rule per line; run it after every edit.
- Interface text needs 4.5:1 contrast on its surface, git decoration colors 3:1 on `--sidebar`, code colors 3:1 on `--editor-surface`. Orca silently drops a pair or a code color below the limit. Fix a failing color by raising its OKLCH lightness only, as little as needed, and record it in the README table "Differences from Bearded".
- A scope with a space or comma (`source.diff markup.inserted`) is skipped. Only `foreground` and `fontStyle` settings are read.

## Done

`python3 -I scripts/check-theme.py` passes, then the checks in `CLAUDE.md`.
