User Documentation
==================

.. toctree::
    :maxdepth: 2

    page_one
    page_two

Overview
--------

`privates` is a library which extends the functionality of python
by exposing previously hidden/private attributes through a nice, easy
API.

No mutations context
^^^^^^^^^^^^^^^^^^^

The ``no_mutations`` context manager throws a MutationError if it detects
a mutation on the passed object within the scope of that context.

::
    from privates import no_mutations

    x = {'a': 1, 'b': 2}

    # This works fine as it's reading
    # from the dictionary
    with no_mutations(x):
        y = x['a']

    # This throws a mutation error because
    # the dict was modified within the context
    with no_mutations(x):
        x['c'] = 3

This behaviour only applies within the scope of the context manager:

::
    from privates import no_mutations

    x = {'a': 1, 'b': 2}

    # This works fine because it is
    # outside the scope of the context
    # manager.
    x['c'] = 3

    # This throws an error
    with no_mutations(x):
        x['d'] = 4

However, even though the error is thrown, the change is still made to
the dictionary:

::
    from privates import no_mutations

    x = {'a': 1, 'b': 2}

    with no_mutations(x):
        x['c'] = 1000

    assert x['c'] == 1000

This is so that any calling code which would like to allow the mutation
can do:

::
    from privates import no_mutations, MutationError

    x = {'a': 1, 'b': 2}

    def my_func(x):
        x['c'] = 3

    try:
        my_func()
    except MutationError:
        pass