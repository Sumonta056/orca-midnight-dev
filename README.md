# Monokai Midnight

A dark Monokai theme for [Orca](https://www.onorca.dev/): an app theme (interface and code colors) and a matching terminal theme. The editor is darker than the sidebars. It is based on [Bearded Theme](https://github.com/BeardedBear/bearded-theme) **Monokai Reversed**, with darker backgrounds.

![Monokai Midnight in Orca](images/cover.png)

Requires Orca 1.4.246 or later.

## Use it

1. Install **Monokai Midnight** from **Settings → Plugins** (community catalog).
2. In **Settings → Appearance**, choose **Monokai Midnight** as the dark theme.
3. In **Settings → Terminal**, choose **Monokai Midnight Terminal**.
4. Optional: install **[Rich Syntax](https://github.com/Sumonta056/orca-rich-syntax)** for Java, Vue, Go, Python, C and C++ files. See [Code colors in Orca](#code-colors-in-orca).

To try a local copy, open **Settings → Plugins → Development folders…** and add this folder.

## Palette

| Role | Hex |
| --- | --- |
| Editor background | `#0c0e13` |
| Sidebar and tabs | `#101219` |
| Text | `#c6cad7` |
| Accent | `#98a2b5` |
| Yellow | `#ffd866` |
| Salmon | `#ff6188` |
| Blue | `#78dce8` |
| Green | `#a9dc76` |
| Turquoise | `#78e8c6` |
| Purple | `#ab9df2` |
| Orange | `#fc9867` |
| Pink | `#e991e3` |
| Red | `#fc6a67` |

Colors come from the built VS Code theme in Bearded Theme 10.1.0 (`bearded-theme-monokai-reversed.json`). All background surfaces are 15% darker in OKLCH lightness than in Bearded.

## Differences from Bearded

Orca needs opaque colors, 4.5:1 contrast for interface text and 3:1 for code colors. Only OKLCH lightness changes, as little as needed.

| Role | Bearded | Here |
| --- | --- | --- |
| Comment | `#4c526b` | `#5a617a` |
| Punctuation | `#c6cad7` at 40% | `#5f626b` |
| Muted interface text | `#c6cad7` at 50% | `#7e818b` |
| Sidebar text | `#a9aec1` at 80% | `#8c90a1` |
| Inactive tab text | `#4c526b` | `#757c97` |

Orca skips scope selectors that contain spaces, such as `source.diff markup.inserted.diff`, so those rules are left out. Simple scopes replace the Markdown and diff rules: headings yellow, inserted green, deleted red, changed blue (the Bearded color for modified files), and tables blue.

## Code colors in Orca

Orca reduces every code token to one of 24 token types before a theme colors it, so a theme in Orca has fewer color groups than in VS Code. Monokai Midnight sets these types to the Bearded colors:

| Token type | Color | Examples |
| --- | --- | --- |
| Keywords and operators | yellow `#ffd866` | `public`, `import`, `if`, `=`, `+` |
| Names (identifiers) | text `#c6cad7` | variables, fields |
| Types | purple `#ab9df2` | `String`, `Order`, Vue components |
| Functions | blue `#78dce8` | `findById`, `useSeo` |
| Strings | green `#a9dc76` | `"text"` |
| Numbers | orange `#fc9867` | `42` |
| Objects, properties, `this` | orange `#fc9867` | `repository.`, `item.title` |
| Constants | red `#fc6a67` | `true`, `null` |
| Parameters, annotations | pink `#e991e3` | `@Component` |
| Regular expressions | turquoise `#78e8c6` | `/^a+$/` |
| Comments | slate italic `#5a617a` | `// note` |

Orca's built-in tokenizers for Java, Vue, Go, Python and C++ give every name the same token. Install [Rich Syntax](https://github.com/Sumonta056/orca-rich-syntax) to color these languages with full TextMate grammars: then types, methods, objects and Vue directives get their own colors, Tailwind class lists turn turquoise, and `function`, `class` and `interface` in Vue scripts turn turquoise as in Bearded. TypeScript and JavaScript files always keep Orca's built-in tokenizer.

## What's new in 1.1.0

- Colors for tabs, git status in the file explorer, the diff view, links, the current workspace row, split dividers and chat messages (23 new interface tokens).
- Code colors adjusted for Orca's token types: yellow keywords and operators, neutral names, orange objects and `this`, pink annotations, turquoise regular expressions.

## License

Monokai Midnight is derived from [Bearded Theme](https://github.com/BeardedBear/bearded-theme) by BeardedBear, licensed under GPL-3.0. It is not an official Bearded Theme release. This theme is also licensed under GPL-3.0.
