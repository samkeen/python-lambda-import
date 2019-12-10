simple Python imports (in the lambda context)

If i do this it works locally: 
`from .foo import goodbye`
https://github.com/samkeen/python-lambda-import/blob/master/hello_world/app.py

but in lambda, I get

```
[ERROR] Runtime.ImportModuleError: Unable to import module 'app': attempted relative import with no known parent package
```

If I hack the syspath with something like

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