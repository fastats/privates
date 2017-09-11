.. privates documentation master file, created by
   sphinx-quickstart on Sat Aug 12 14:53:44 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to `privates` documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   changelog

Overview
--------

`privates` is a library which extends the functionality of python
by exposing previously hidden/private attributes through a nice, easy
API.

This library was created to have a thoroughly tested community resource
for the helper functions we sometimes need in our applications, but which
involve private/hidden attributes.

No mutations context
^^^^^^^^^^^^^^^^^^^^

The :func:`~privates.mutations.no_mutations` context manager throws a :class:`~privates.core.errors.MutationError` if it detects
a mutation on the passed object within the scope of that context:

.. doctest::

    >>> from privates import no_mutations
    >>> x = {'a': 1, 'b': 2}
    >>>
    >>> # This works fine as it's reading
    >>> # from the dictionary
    >>> with no_mutations(x):
    ...     y = x['a']
    >>>
    >>> # This throws a mutation error because
    >>> # the dict was modified within the context
    >>> with no_mutations(x):
    ...    x['c'] = 3
    Traceback (most recent call last):
        ...
    privates.core.errors.MutationError: The dict was mutated

This behaviour only applies within the scope of the context manager:

.. doctest::

    >>> from privates import no_mutations
    >>> x = {'a': 1, 'b': 2}
    >>>
    >>> # This works fine because it is
    >>> # outside the scope of the context
    >>> # manager.
    >>> x['c'] = 3
    >>>
    >>> # This throws an error
    >>> with no_mutations(x):
    ...    x['d'] = 4
    Traceback (most recent call last):
        ...
    privates.core.errors.MutationError: The dict was mutated

However, even though the error is thrown, the change is still made to
the dictionary:

.. doctest::

    >>> from privates import no_mutations
    >>> x = {'a': 1, 'b': 2}
    >>> with no_mutations(x):
    ...    x['c'] = 1000
    Traceback (most recent call last):
        ...
    privates.core.errors.MutationError: The dict was mutated
    >>> assert x['c'] == 1000

This is so that any calling code which would like to allow the mutation
can do:

.. doctest::

    >>> from privates import no_mutations, MutationError
    >>> x = {'a': 1, 'b': 2}
    >>> def my_func(x):
    ...    x['c'] = 3
    >>> try:
    ...     my_func(x)
    ... except MutationError:
    ...     pass


NamedStruct
^^^^^^^^^^^

The :class:`privates.named_struct.NamedStruct` is a typed struct class which allows inheritance (unlike `tuple`/`typing.NamedTuple`), and which
can be automatically converted to an instance of a :ref:`numba.jitclass`
using its classmethod `.create(**kwargs)`.

A simple 2D Point and Rectangle class can therefore be defined as follows:

.. doctest::

    >>> from numba.types import float64
    >>> from privates import NamedStruct
    >>>
    >>> class Point(NamedStruct):
    ...     x: float64
    ...     y: float64
    ...
    ...     def distance_from_origin(self):
    ...         return np.sqrt(self.x**2 + self.y**2)
    >>>
    >>> class Rectangle(Point):
    ...     width: float64
    ...     height: float64
    ...     
    ...     def area(self):
    ...         return self.width * self.height
    >>>
    >>> p = Point(x=1, y=1)
    >>> p.distance_from_origin()
    1.414...
    >>> r = Rectangle(x=0, y=0, height=5, width=4)
    >>> r.area()
    20.0

The attributes and methods from Point are inherited by Rectangle, and the use of `numba.types` as the type declarations allows jitclasses to be used
directly without extra decorators:

.. doctest::

    >>> from numba.types import float64
    >>> from privates import NamedStruct
    >>>
    >>> class Point(NamedStruct):
    ...     x: float64
    ...     y: float64
    >>> 
    >>> p = Point.create(x=3, y=4)
    >>> p.distance_from_origin()
    5.0


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
