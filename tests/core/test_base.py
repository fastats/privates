
import ctypes

from privates.core import PyObjectStruct


def test_pyobjectstruct_size():
    py_size = object.__basicsize__
    ct_size = ctypes.sizeof(PyObjectStruct)
    assert py_size == ct_size
