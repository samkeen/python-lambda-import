# Imports (that work in the Lambda context)

This is a simple workbook repo for testing strategies.

## Current Strategy
Hack the path in the test runner

Use this import: `from .lib.foo import goodbye`.  This will work as in in the Lambda context

Test run will fail with `ModuleNotFoundError: No module named 'lib'`

So in `conftest.py` hack the syspath
```python
import os, sys
from os.path import join

lambda_dir = join(os.path.dirname(os.path.abspath(__file__)), 'hello_world')
sys.path.append(lambda_dir)
```

Happy Tests (and happy lambda)
```bash
pytest
======================== test session starts ===============================
platform darwin -- Python 3.7.4, pytest-5.3.1, py-1.8.0, pluggy-0.13.1
rootdir: /Users/samkeen/Projects/pyhon-import-test
collected 1 item                                                                                                                                                                              

tests/unit/test_handler.py .                                                                                                                                                            [100%]

======================== 1 passed in 0.02s =================================
```

## Other things tried

_Note, for me when I say "works locally", I mean I can run the tests_


Relative imports works locally: 
`from .foo import goodbye`
https://github.com/samkeen/python-lambda-import/blob/master/hello_world/app.py

but in lambda, I get
```
[ERROR] Runtime.ImportModuleError: Unable to import module 'app': attempted relative import with no known parent package
```

If I hack the syspath in the lambda file with something like

```
import os, sys
this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_dir)

# get rid of '.'
from foo import goodbye
```
https://github.com/samkeen/python-lambda-import/blob/hack-syspath/hello_world/app.py

It works locally and in Lambda, but it just seems dirty

What am I missing here???  Is there a non-syspath hacked strategy that works locally and in the lambda context?

## References

https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
https://napuzba.com/a/import-error-relative-no-parent/p2
https://stackoverflow.com/questions/53819914/trouble-loading-local-modules-only-with-aws-lambda
https://gist.github.com/gene1wood/06a64ba80cf3fe886053f0ca6d375bc0
