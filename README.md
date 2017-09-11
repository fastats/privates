# privates

[![Build Status](https://travis-ci.org/fastats/privates.svg?branch=master)](https://travis-ci.org/fastats/privates)
[![Documentation Status](https://readthedocs.org/projects/privates/badge/?version=latest)](http://privates.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/fastats/privates/branch/master/graph/badge.svg)](https://codecov.io/gh/fastats/privates)

A python library using private/hidden python language features

[Click here for the documentation](http://privates.readthedocs.io/en/latest/)

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

- A `NamedStruct` to facilitate calling external native/jitted APIs, which
allows inheritance of attributes, among other behaviours. This also features
as a better `namedtuple`/`typing.NamedTuple`, without the errors  and performance
issues of the existing implementations.

```python
from privates import NamedStruct


class Point(NamedStruct):
    x: int
    y: int


class Rectangle(Point):
    height: int
    width: int

    def area(self):
        return self.height * self.width


# This creates a `numba` jitclass.
r = Rectangle.create(x=0, y=0, height=3, width=4)
assert r.area() == 12
```

## development/contributing

- To report a bug, please open a PR with a new (failing) unit-test showing the
problem.
- To request a feature, please open a PR with a new (failing) unit-test showing
the preferred API.
- To make a contribution, please open a PR with new (passing) unit-tests,
inline doctest examples and documentation updates.


## requirements

- Python 3.6 or later
- py.test
- coverage

### optional requirements

- numba >= 0.33

