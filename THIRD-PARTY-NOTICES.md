# Third-party notices

Monokai Midnight ships TextMate grammars and language configuration files from the [Visual Studio Code](https://github.com/microsoft/vscode) repository at `4d2fba6576fd008ecfcc06a93378d004460c2473`, and the Vue grammar from [vuejs/language-tools](https://github.com/vuejs/language-tools) at `c59f9908b4912ee20141b53a99b1ce485bff0dc7`.

Changes from the original files:

- References to rules that do not exist are removed (`#string_context` in `c.tmLanguage.json`, `#tags` in `html-vue.tmLanguage.json`). VS Code ignores those references.
- `html-vue.tmLanguage.json` includes the Vue interpolation and directive rules at the start of its top-level and `attribute` patterns. In VS Code, the Vue extension adds them with injection grammars, which Orca does not support.
- Some scope names are renamed, because Orca reduces every scope to one of 24 token types and the original names land on the wrong type. The full list is in `scripts/remap-scopes.py`.
- The language configuration files are converted to strict JSON with only the keys that Orca reads.

## redhat-developer/vscode-java

- Source: https://github.com/redhat-developer/vscode-java (`f09b712f5d6d6339e765f58c8dfab3f78a378183`, version 1.26.0)
- License: MIT
- Used in: `java.tmLanguage.json`

```
Copyright (c) 2014 GitHub Inc.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

--------------------------------------------------------------------

This package was derived from a TextMate bundle located at
https://github.com/textmate/java.tmbundle and distributed under the following
license, located in `README.mdown`:

Permission to copy, use, modify, sell and distribute this
software is granted. This software is provided "as is" without
express or implied warranty, and with no claim as to its
suitability for any purpose.
```

## worlpaker/go-syntax

- Source: https://github.com/worlpaker/go-syntax (`c74e22eb9ef32958e3edd130ea750ce78d8b8241`, version 0.8.6)
- License: MIT
- Used in: `go.tmLanguage.json`

```
MIT License

Copyright (c) 2023 Furkan Ozalp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## MagicStack/MagicPython

- Source: https://github.com/MagicStack/MagicPython (`7d0f2b22a5ad8fccbd7341bc7b7a715169283044`, version 1.1.1)
- License: MIT
- Used in: `python.tmLanguage.json, regexp-python.tmLanguage.json`

```
The MIT License

Copyright (c) 2015-present MagicStack Inc.  http://magic.io

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## jeff-hykin/better-cpp-syntax

- Source: https://github.com/jeff-hykin/better-cpp-syntax (`071dd6ecc9eda347bd84c8aa0e0b557396cb6a40`, version 1.27.1)
- License: MIT
- Used in: `cpp.tmLanguage.json, cpp-embedded-macro.tmLanguage.json`

```
MIT License

Copyright (c) 2019 Jeff Hykin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## jeff-hykin/better-c-syntax

- Source: https://github.com/jeff-hykin/better-c-syntax (`34712a6106a4ffb0a04d2fa836fd28ff6c5849a4`, version 1.13.2)
- License: MIT
- Used in: `c.tmLanguage.json`

```
MIT License

Copyright (c) 2019 Jeff Hykin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## textmate/c.tmbundle

- Source: https://github.com/textmate/c.tmbundle (`60daf83b9d45329524f7847a75e9298b3aae5805`, version 0.0.0)
- License: TextMate Bundle License
- Used in: `c.tmLanguage.json (original grammar)`

```
Copyright (c) textmate-c.tmbundle authors

If not otherwise specified (see below), files in this repository fall under the following license:

Permission to copy, use, modify, sell and distribute this
software is granted. This software is provided "as is" without
express or implied warranty, and with no claim as to its
suitability for any purpose.

An exception is made for files in readable text which contain their own license information,
or files where an accompanying file exists (in the same directory) with a "-license" suffix added
to the base-name name of the original file, and an extension of txt, html, or similar. For example
"tidy" is accompanied by "tidy-license.txt".
```

## microsoft/TypeScript-TmLanguage

- Source: https://github.com/microsoft/TypeScript-TmLanguage (`48f608692aa6d6ad7bd65b478187906c798234a8`, version 1.0.0)
- License: MIT
- Used in: `typescript.tmLanguage.json, javascript.tmLanguage.json`

```
Copyright (c) Microsoft Corporation
All rights reserved.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## textmate/javascript.tmbundle

- Source: https://github.com/textmate/javascript.tmbundle (`fccf0af0c95430a42e1bf98f0c7a4723a53283e7`, version 0.0.0)
- License: TextMate Bundle License
- Used in: `javascript.tmLanguage.json (original grammar)`

```
Copyright (c) textmate-javascript.tmbundle project authors

If not otherwise specified (see below), files in this repository fall under the following license:

Permission to copy, use, modify, sell and distribute this
software is granted. This software is provided "as is" without
express or implied warranty, and with no claim as to its
suitability for any purpose.

An exception is made for files in readable text which contain their own license information,
or files where an accompanying file exists (in the same directory) with a "-license" suffix added
to the base-name name of the original file, and an extension of txt, html, or similar. For example
"tidy" is accompanied by "tidy-license.txt".
```

## microsoft/vscode-css

- Source: https://github.com/microsoft/vscode-css (`de9e6beee756760f31b15efbd782735fc25de3db`, version 0.0.0)
- License: MIT License
- Used in: `css.tmLanguage.json`

```
MIT License

Copyright (c) Microsoft Corporation.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

--------------------------------------------------------------------

This package was derived from a TextMate bundle located at
https://github.com/textmate/css.tmbundle and distributed under the following
license, located in `README.mdown`:

Permission to copy, use, modify, sell and distribute this
software is granted. This software is provided "as is" without
express or implied warranty, and with no claim as to its
suitability for any purpose.
```

## atom/language-sass

- Source: https://github.com/atom/language-sass (`303bbf0c250fe380b9e57375598cfd916110758b`, version 0.61.4)
- License: MIT
- Used in: `scss.tmLanguage.json`

```
Copyright (c) 2014 GitHub Inc.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

--------------------------------------------------------------------

This package was derived from a TextMate bundle located at
https://github.com/alexsancho/Sass.tmbundle and distributed under the following
license, located in `LICENSE.md`:

Copyright (c) 2012 Alex Sancho, http://alexsancho.name/

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## textmate/html.tmbundle

- Source: https://github.com/textmate/html.tmbundle (`0c3d5ee54de3a993f747f54186b73a4d2d3c44a2`, version 0.0.0)
- License: TextMate Bundle License
- Used in: `html-vue.tmLanguage.json`

```
Copyright (c) textmate-html.tmbundle project authors

If not otherwise specified (see below), files in this repository fall under the following license:

Permission to copy, use, modify, sell and distribute this
software is granted. This software is provided "as is" without
express or implied warranty, and with no claim as to its
suitability for any purpose.

An exception is made for files in readable text which contain their own license information,
or files where an accompanying file exists (in the same directory) with a "-license" suffix added
to the base-name name of the original file, and an extension of txt, html, or similar. For example
"tidy" is accompanied by "tidy-license.txt".
```

## vuejs/language-tools

- Source: https://github.com/vuejs/language-tools (`c59f9908b4912ee20141b53a99b1ce485bff0dc7`)
- License: MIT
- Used in: `vue.tmLanguage.json`, `vue.language-configuration.json`

```
MIT License

Copyright (c) 2021-present Johnson Chu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## microsoft/vscode

- Source: https://github.com/microsoft/vscode (`4d2fba6576fd008ecfcc06a93378d004460c2473`)
- License: MIT
- Used in: all files in `syntaxes/` except the Vue files

```
MIT License

Copyright (c) 2015 - present Microsoft Corporation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
