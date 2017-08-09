

class MutationError(Exception):
    """
    Raised when an object was mutated, or
    an attempt was made to mutate it during
    an immutable context.
    """


if __name__ == '__main__':
    import pytest
    pytest.main()
