
import pytest

from privates import NamedStruct


class First(NamedStruct):
    a: int
    b: str


class Second(First):
    c: float
    d: str


class Third(Second):
    e: int
    f: str


class Fourth(Third):
    g: str
    h: int


def test_attribute_order():
    f = Fourth(1, 'a', 2.0, 'b', 3, 'c', 'test', 30_000)

    assert f.a == 1
    assert f[0] == 1

    assert f.b == 'a'
    assert f[1] == 'a'

    assert f.c == 2.0
    assert f[2] == 2.0

    assert f.d == 'b'
    assert f[3] == 'b'

    assert f.e == 3
    assert f[4] == 3

    assert f.f == 'c'
    assert f[5] == 'c'

    assert f.g == 'test'
    assert f[6] == 'test'

    assert f.h == 30000
    assert f[7] == 30000

    with pytest.raises(IndexError):
        _ = f[8]


def test_types_are_validated():
    with pytest.raises(AssertionError):
        f = Fourth('1', 'a', 2.0, 'b', 3, 'c', 'test', 30_000)
        
