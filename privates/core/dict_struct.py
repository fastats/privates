
import ctypes

from privates.core.base import PyObjectStruct


class DictStruct(PyObjectStruct):
    """
    Mirrors the structure behind the `PyDictObject`
    definition in CPython.
    CPython: Include/dictobject.h#L23-L41
    """
    _fields_ = [
        ('ma_used', ctypes.c_ssize_t),
        ('ma_version_tag', ctypes.c_uint64),
        ('ma_keys', ctypes.c_void_p),
        ('ma_values', ctypes.c_void_p)
    ]

    def __repr__(self):
        return (
            f"DictStruct(size={self.ma_used}, "
            f"refcount={self.ob_refcnt}, "
            f"version={self.ma_version_tag})"
        )

    @classmethod
    def from_dict(cls, obj):
        assert isinstance(obj, dict)
        return cls.from_address(id(obj))

    @property
    def size(self):
        return self.ma_used

    @property
    def version(self):
        return self.ma_version_tag

    @property
    def ref_count(self):
        return self.ob_refcnt


if __name__ == '__main__':
    import pytest
    pytest.main()