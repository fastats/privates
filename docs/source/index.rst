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



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
