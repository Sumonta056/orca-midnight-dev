#!/usr/bin/env bash
set -euo pipefail

OUT="$(cd "$(dirname "$0")/.." && pwd)/syntaxes"
VSCODE_COMMIT="${1:-$(cat "${OUT}/VSCODE_COMMIT")}"
VUE_COMMIT="${2:-$(cat "${OUT}/VUE_COMMIT")}"
VSCODE="https://raw.githubusercontent.com/microsoft/vscode/${VSCODE_COMMIT}/extensions"
VUE="https://raw.githubusercontent.com/vuejs/language-tools/${VUE_COMMIT}/extensions/vscode"

fetch() {
  curl -fsSL "$1" -o "${OUT}/$2"
  echo "${2}"
}

fetch "${VSCODE}/java/syntaxes/java.tmLanguage.json" java.tmLanguage.json
fetch "${VSCODE}/java/language-configuration.json" java.language-configuration.json
fetch "${VSCODE}/go/syntaxes/go.tmLanguage.json" go.tmLanguage.json
fetch "${VSCODE}/go/language-configuration.json" go.language-configuration.json
fetch "${VSCODE}/python/syntaxes/MagicPython.tmLanguage.json" python.tmLanguage.json
fetch "${VSCODE}/python/syntaxes/MagicRegExp.tmLanguage.json" regexp-python.tmLanguage.json
fetch "${VSCODE}/python/language-configuration.json" python.language-configuration.json
fetch "${VSCODE}/cpp/syntaxes/cpp.tmLanguage.json" cpp.tmLanguage.json
fetch "${VSCODE}/cpp/syntaxes/cpp.embedded.macro.tmLanguage.json" cpp-embedded-macro.tmLanguage.json
fetch "${VSCODE}/cpp/syntaxes/c.tmLanguage.json" c.tmLanguage.json
fetch "${VSCODE}/cpp/language-configuration.json" cpp.language-configuration.json
fetch "${VSCODE}/typescript-basics/syntaxes/TypeScript.tmLanguage.json" typescript.tmLanguage.json
fetch "${VSCODE}/javascript/syntaxes/JavaScript.tmLanguage.json" javascript.tmLanguage.json
fetch "${VSCODE}/css/syntaxes/css.tmLanguage.json" css.tmLanguage.json
fetch "${VSCODE}/scss/syntaxes/scss.tmLanguage.json" scss.tmLanguage.json
fetch "${VSCODE}/html/syntaxes/html.tmLanguage.json" html-vue.tmLanguage.json
fetch "${VUE}/syntaxes/vue.tmLanguage.json" vue.tmLanguage.json
fetch "${VUE}/languages/vue-language-configuration.json" vue.language-configuration.json

python3 -I "$(dirname "$0")/convert-config.py" "${OUT}"/*.language-configuration.json
python3 -I "$(dirname "$0")/drop-broken-includes.py" "${OUT}"/*.tmLanguage.json
python3 -I "$(dirname "$0")/patch-html-for-vue.py" "${OUT}/html-vue.tmLanguage.json"
python3 -I "$(dirname "$0")/remap-scopes.py" "${OUT}"/*.tmLanguage.json

echo "${VSCODE_COMMIT}" > "${OUT}/VSCODE_COMMIT"
echo "${VUE_COMMIT}" > "${OUT}/VUE_COMMIT"
