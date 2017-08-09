
import ctypes

from privates.core import DictStruct


def test_dict_struct_size():
    di_size = dict.__basicsize__
    ct_size = ctypes.sizeof(DictStruct)
    assert di_size == ct_size


def test_size_property():
    x = dict(a=1)
    ds = DictStruct.from_dict(x)
    assert ds.size == 1

    x['b'] = 2
    assert ds.size == 2


def test_version_increases_on_mutation():
    x = dict(a=1)
    ds = DictStruct.from_dict(x)
    assert ds.size == 1

    initial = ds.version
    x['b'] = 2
    assert initial < ds.version


def test_ref_count_constant():
    x = dict(a=1)
    ds = DictStruct.from_dict(x)
    initial = ds.ref_count
    assert 0 < initial

    x['b'] = 2
    assert initial == ds.ref_count


def test_ref_count_increases():
    x = dict(a=1)
    ds = DictStruct.from_dict(x)
    initial = ds.ref_count
    assert 0 < initial

    y = x
    assert initial + 1 == ds.ref_count


if __name__ == '__main__':
    import pytest
    pytest.main()