---
paths:
  - "syntaxes/**"
  - "scripts/**"
---

# Grammars

## Source of truth

`syntaxes/` is generated. Change a script in `scripts/`, then regenerate:

```sh
./scripts/update-grammars.sh
```

It downloads every grammar from the commits in `syntaxes/VSCODE_COMMIT` and `syntaxes/VUE_COMMIT`, then runs, in order: `convert-config.py`, `drop-broken-includes.py`, `patch-html-for-vue.py`, `remap-scopes.py`. A hand edit in `syntaxes/` is lost on the next run. Pass two commit SHAs to update the upstream grammars; then refresh `THIRD-PARTY-NOTICES.md`.

## Orca behaviors behind each script

- **Strict configuration files.** Orca reads only `comments`, `brackets`, `autoClosingPairs` and `surroundingPairs`, as strict JSON, with pairs as `{"open", "close"}` objects. A bracket pair equal to the block comment markers makes the rainbow bracket colors paint `<!--` and `-->`, so `convert-config.py` removes it.
- **Broken includes.** A `#rule` include that names no repository entry makes Orca refuse the whole plugin when it loads (status `errored`), although `orca plugin validate` passes. VS Code ignores such an include; `drop-broken-includes.py` removes it. An include of a scope outside the plugin (`source.yaml`) is allowed and stays plain.
- **No injection grammars.** Orca reads only `scopeName`, `patterns`, `repository` and rule keys. Vue's directives, `{{ }}` interpolation and the `class` list rule are therefore patched straight into the HTML copy by `patch-html-for-vue.py`.
- **24 token types.** Orca reduces every scope to one type before the theme colors it (table in `.claude/rules/theme.md`). `remap-scopes.py` renames scopes that land on the wrong type, for example `storage.type.java` (Orca: keyword) to `support.type.java` (Orca: type). Some renames borrow a type for its color: Tailwind class lists and `function`/`class`/`interface` use `regexp` because the theme colors it turquoise, as Bearded colors them.
- **No type means fallback.** A scope that maps to no type produces no token, and Orca shows its built-in tokenizer's color there. Give every visible word a scope with a type; `meta.*` alone is never enough.
- **Protected languages.** Orca keeps its own tokenizer for TypeScript, JavaScript, JSON, CSS, SCSS, Less, HTML and Markdown files. The TS, JS, CSS, SCSS and HTML grammars here claim no extensions; they color only blocks inside `.vue` files.
- **Limits.** At most 16 syntaxes, 1 MiB per grammar, 64 KiB per configuration. A line over 1,000 characters or 50 ms leaves the rest of the file plain.

## Check a scope change

Tokenize a sample with the shipped grammars before asking the user for a screenshot. Shiki (`createHighlighter`, `getLanguage(...).tokenizeLine`) runs the same `vscode-textmate` engine and Oniguruma that Orca's worker uses. Map the innermost scope through the legend in `.claude/rules/theme.md`, skipping `punctuation.*` scopes, and confirm the word lands on the intended type.

## Done

`./scripts/update-grammars.sh` runs clean, `orca plugin validate .` passes, and after `orca plugin dev reload "$PWD"` the plugin shows `idle`, not `errored`.
