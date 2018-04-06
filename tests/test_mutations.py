
import pytest

from privates import no_mutations, MutationError


def test_no_mutations_valid():
    x = dict(a=1)

    with no_mutations(x):
        test = x['a']
    assert test == 1


def test_dict_mutation_raises():
    x = dict(a=1)

    with pytest.raises(MutationError):
        with no_mutations(x):
            x['b'] = 2
    # MutationError was raised, but
    # mutation still exists.
    assert 'b' in x


def test_multiple_reads_valid():
    x = dict(a=1)

    with no_mutations(x):
        test = x['a']
    assert test == 1

    with no_mutations(x):
        second = x['a']
    assert test == second


def test_non_context_mutations():
    x = dict(a=1)

    with no_mutations(x):
        test = x['a']
    assert test == 1

    x['b'] = 2

    with no_mutations(x):
        first = x['a']
        second = x['b']

    assert first == 1
    assert second == 2


def test_multi_non_context_mutations():
    x = dict(a=1)
    x['b'] = 2

    with no_mutations(x):
        first = x['a']
    assert first == 1

    x['c'] = 3

    with no_mutations(x):
        second = x['b']
    assert second == 2

    x['d'] = 4

    with no_mutations(x):
        third = x['c']
    assert third == 3


def test_key_error_still_raises():
    x = dict(a=1)

    with pytest.raises(KeyError):
        with no_mutations(x):
            _ = x['b']


def test_other_mutations_valid():
    x = dict(a=1, b=2)
    other = {}

    with no_mutations(x):
        for k, v in x.items():
            other[k] = v

    assert other['a'] == 1
    assert other['b'] == 2


def test_replace_is_invalid():
    x = dict(a=1, b=2)

    with pytest.raises(MutationError):
        with no_mutations(x):
            del x['b']
            x['b'] = 2

    with pytest.raises(MutationError):
        with no_mutations(x):
            del x['a']
            x['a'] = 1


def test_string_values():
    x = dict(a='a', b='b')

    with no_mutations(x):
        test = x['a']
    assert test == 'a'

    with pytest.raises(MutationError):
        with no_mutations(x):
            x['c'] = 'c'
    assert 'c' in x


def test_tuple_keys():
    x = { ('a', 'b'): 1, ('c', 'd'): 2}

    with no_mutations(x):
        test = x[('a', 'b')]
    assert test == 1

    with pytest.raises(MutationError):
        with no_mutations(x):
            x[('e', 'f')] = 3
    assert ('e', 'f') in x


def test_mutation_in_function():
    x = {'a': 1, 'b': 2}

    def my_func(a):
        a['c'] = 3

    with pytest.raises(MutationError):
        with no_mutations(x):
            my_func(x)


if __name__ == '__main__':
    pytest.main([__file__])
