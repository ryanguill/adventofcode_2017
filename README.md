# adventofcode_2017
My 2017 advent of code python repo

I am using python because it is a language I do not know - I do not submit this as idiomatic code, or even good code!

My goal is not to golf the code or even get on the leaderboard, just to write functional programs that get the right answer
and attempt to do so with maintainable solutions, while learning the language and its idioms along the way.

To test:
`$ pytest`

With my pytest.ini configuration, tests can be in any .py file but must be a function starting with `def test_`

utils are in `lib/utils.py`, but because of python strangeness, to import them in the day files I have to use

```
import sys
sys.path.append(sys.path[0] + "/..")

from lib.utils import read_input
```

(if anyone knows better than that, please let me know.)


My vscode workspace settings:
```
{
	"editor.insertSpaces": false,
	"editor.tabSize": 4,
	"files.exclude": {
		"**/.git": true,
		"**/.svn": true,
		"**/.hg": true,
		"**/CVS": true,
		"**/.DS_Store": true,
		"**/*__pycache__": true,
		"**/.cache": true
	},
	"files.trimTrailingWhitespace": true
}
```