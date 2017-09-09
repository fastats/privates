# privates

[![Build Status](https://travis-ci.org/fastats/privates.svg?branch=master)](https://travis-ci.org/fastats/privates)
[![codecov](https://codecov.io/gh/fastats/privates/branch/master/graph/badge.svg)](https://codecov.io/gh/fastats/privates)


A python library using private/hidden python language features


## features

- Dictionary mutation checker (Python 3.6 only), inspired by [Jake
VanderPlas' excellent post](https://jakevdp.github.io/blog/2017/05/26/exposing-private-dict-version/)
about python 3.6's private dict version.

```python
from privates import no_mutations

x = {a: 1, b: 2}

with no_mutations(x):
    value = x['a']  # this is fine

with no_mutations(x):
    x['c'] = 3  # this will throw a MutationError

# The mutation check is `ex-post`,
# therefore the change is still made.
assert 'c' in x
```


## requirements

- Python 3.6 or later
- Py.test
- coverage
