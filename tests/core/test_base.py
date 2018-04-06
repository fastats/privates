
import ctypes

from privates.core import PyObjectStruct


def test_pyobjectstruct_size():
    py_size = object.__basicsize__
    ct_size = ctypes.sizeof(PyObjectStruct)
    assert py_size == ct_size


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
