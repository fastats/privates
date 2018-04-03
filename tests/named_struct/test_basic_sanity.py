
from collections import OrderedDict

import pytest

from privates import NamedStruct


class MyStruct(NamedStruct):
    a: int
    b: int
    c: float


def test_iter_support():
    m = MyStruct(1, 2, 3.0)
    fields = list(m)

    assert isinstance(fields[0], tuple)
    assert fields[0][0] == 'a'
    assert fields[0][1] == int
    assert fields[1][0] == 'b'
    assert fields[1][1] == int
    assert fields[2][0] == 'c'
    assert fields[2][1] == float

    with pytest.raises(IndexError):
        _ = fields[3]

def test_ordered_dict_support():
    m = MyStruct(1, 2, 3.0)
    od = OrderedDict(m)

    assert od['a'] == int
    assert od['b'] == int
    assert od['c'] == float

    with pytest.raises(KeyError):
        _ = od['d']


def test_tuple_indexing():
    m = MyStruct(2, 3, 4.0)

    assert m[0] == 2
    assert m[1] == 3
    assert m[2] == 4.0

    with pytest.raises(IndexError):
        _ = m[3]


def test_insufficient_args():
    with pytest.raises(AssertionError):
        _ = MyStruct(1)


def test_too_many_args():
    with pytest.raises(AssertionError):
        _ = MyStruct(1, 2, 3.0, 4)


def test_items():
    view = MyStruct.items()
    items = dict(view)

    assert 'a' in items
    assert 'b' in items
    assert 'c' in items


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
