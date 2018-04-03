
from typing import Optional, Any, Iterator


class NamedStruct:
    """
    ``NamedStruct`` is a class which facilitates interactions
    between raw python code and native/jitted code.

    A single ``NamedStruct`` definition can be used as an
    argument for:
    - a `numba` jitclass.
    - TODO: a native function which takes a `ctypes` struct.
    - TODO: a `cffi` function which requires a native C pointer.

    As a side effect, this is also a better NamedTuple, without
    all the problems of ``namedtuple`` or ``typing.NamedTuple``

    Examples
    --------
    A `numba` jitclass.
    >>> from privates import NamedStruct
    >>> class MyStruct(NamedStruct):
    ...     a: int
    ...     b: int
    ...     c: float
    >>> m = MyStruct(1, 2, 3.0)
    >>> m.a
    1
    >>> m.b
    2
    >>> m.c
    3.0

    """
    def __init__(self, *args):
        fields = self._fields()
        assert len(fields) == len(args), "Invalid Arguments"
        for (name, typ), value in zip(fields.items(), args):
            assert isinstance(value, typ), f"{name} is not a {typ}"
            setattr(self, name, value)

    @classmethod
    def _fields(cls) -> dict:
        init = {}
        for base in reversed(cls.mro()):
            try:
                init.update(base.__annotations__ or {})
            except AttributeError: # no annotations
                continue
        init.update(cls.__annotations__)
        return init

    def __iter__(self) -> Iterator:
        """
        Implementing this makes the NamedStruct iterable.

        This means that looping over the struct object (such
        as in an OrderedDict constructor) will visit this
        method.

        The implementation returns an iterator over the
        `__annotations__` mapping which is inherited from
        all base classes.

        >>> from privates import NamedStruct
        >>> class MyStruct(NamedStruct):
        ...     a: int
        >>> m = MyStruct(30_000)
        >>> list(m)
        [('a', <class 'int'>)]
        """
        return iter(self._fields().items())

    def __getitem__(self, key) -> Optional[Any]:
        """
        Implementing this overrides the default behaviour
        for square-bracket-indexing, ie, my_obj[0].

        In this case we accept integer indices to represent
        the struct attributes, with the order being the
        order they are defined on this class.

        >>> from privates import NamedStruct
        >>> class Test(NamedStruct):
        ...     a: int
        ...     b: float
        >>> t = Test(1, 2.0)
        >>> t[0]
        1
        >>> t[1]
        2.0
        """
        item = list(self._fields())[key]
        name = item[0]
        return getattr(self, name)

    def __len__(self) -> int:
        """
        Implementing this allows us to call the builtin `len`
        on our objects.

        The value returned is an integer count of the number
        of fields defined on the struct.

        >>> from privates import NamedStruct
        >>> class First(NamedStruct):
        ...     a: int
        ...     b: int
        >>> class Second(First):
        ...     c: float
        >>> f = First(1, 2)
        >>> len(f)
        2
        >>> s = Second(1, 2, 3.0)
        >>> len(s)
        3
        """
        return sum(1 for _ in iter(self))

    @classmethod
    def items(cls):
        """
        This mimics the `dict` API, which is required for
        `numba` support.

        When passing an object to the `jitclass` decorator in
        `numba`, `numba` does `OrderedDict(my_obj)` to get the
        attribute and type specifications, which requires us to
        have this implemented.

        >>> from privates import NamedStruct
        >>> class Test(NamedStruct):
        ...     a: int
        ...     b: int
        >>> t = Test(1, 2)
        >>> t.items()
        dict_items([('a', <class 'int'>), ('b', <class 'int'>)])
        """
        return cls._fields().items()

    @classmethod
    def create(cls, **kwargs):
        jit_cls = cls._gen_type()
        args = (kwargs[k] for k, _ in cls.items())
        return jit_cls(*args)

    @classmethod
    def _gen_type(cls):
        from numba import jitclass  # Lazy import
        latest = object
        fields = cls._fields()
        for base in reversed(cls.mro()):
            if base is not NamedStruct:
                # TODO: generate __init__ for annotations
                items = {'__init__': base.__dict__.get('__init__')}
                meths = {k: v for k, v in base.__dict__.items()
                         if not k.startswith('__')}
                items.update(meths)
                latest = type(str(base), (latest,), items)
        return jitclass(fields)(latest)
