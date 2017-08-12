
import ctypes


class PyObjectStruct(ctypes.Structure):
    """
    A `ctypes.Structure` which mirrors the
    base structure of the `object` type in
    CPython.

    >>> ob_size = object.__basicsize__
    >>> ct_size = ctypes.sizeof(PyObjectStruct)
    >>> ob_size == ct_size
    True
    """
    _fields_ = [
        ('ob_refcnt', ctypes.c_ssize_t),
        ('ob_type', ctypes.c_void_p)
    ]
