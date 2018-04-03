
import pytest

from privates import NamedStruct


class First(NamedStruct):
    a: int
    b: float


class Second(First):
    b: int
    c: str


def test_overridden_attribute():
    s = Second(1, 2, 'test')

    assert len(s) == 3

    assert s.a == 1
    assert s[0] == 1

    assert s.b == 2
    assert s[1] == 2

    assert s.c == 'test'
    assert s[2] == 'test'

    with pytest.raises(IndexError):
        _ = s[3]


def test_previous_attribute_type_fails():
    f = First(1, 2.0)

    assert len(f) == 2
    assert f.a == 1
    assert f[0] == 1
    assert f.b == 2.0
    assert f[1] == 2.0

    with pytest.raises(AssertionError):
        _ = Second(1, 2.0, 'test')


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
