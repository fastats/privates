
from contextlib import contextmanager

from privates.core import DictStruct, MutationError


@contextmanager
def no_mutations(obj):
    """
    A context manager that ensures no
    mutations are made to a dictionary
    within its context.

    If mutations are made, an AssertionError
    is raised.

    >>> x = dict(a=1)
    >>> with no_mutations(x):
    ...     test = x['a']
    >>> with no_mutations(x):
    ...     x['b'] = 'test'
    Traceback (most recent call last):
        ...
    privates.core.errors.MutationError: The dict was mutated
    """
    assert isinstance(obj, dict)
    ds = DictStruct.from_dict(obj)
    initial = ds.version
    try:
        yield obj
    finally:
        if initial < ds.version:
            raise MutationError('The dict was mutated')


if __name__ == '__main__':
    import pytest
    pytest.main()