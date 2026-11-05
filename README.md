# Monokai Midnight

A dark Monokai theme for [Orca](https://www.onorca.dev/): an app theme (interface and code colors) and a matching terminal theme. The editor is darker than the sidebars. It is based on [Bearded Theme](https://github.com/BeardedBear/bearded-theme) **Monokai Reversed**, with darker backgrounds.

![Monokai Midnight in Orca](images/cover.png)

Requires Orca 1.4.246 or later.

## Use it

1. Open **Settings → Plugins → Development folders…** and add this folder.
2. In **Settings → Appearance**, choose **Monokai Midnight** as the dark theme.
3. In **Settings → Terminal**, choose **Monokai Midnight Terminal**.

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

Orca skips scope selectors that contain spaces, such as `source.diff markup.inserted.diff`, so those rules are left out. Simple scopes replace the Markdown and diff rules: headings yellow, inserted green, deleted red, changed blue (the Bearded color for modified files), and tables blue.

## License

Monokai Midnight is derived from [Bearded Theme](https://github.com/BeardedBear/bearded-theme) by BeardedBear, licensed under GPL-3.0. It is not an official Bearded Theme release. This theme is also licensed under GPL-3.0.
