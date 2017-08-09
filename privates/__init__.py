
import sys
assert (3, 6) <= sys.version_info

from privates.core.errors import MutationError
from privates.mutations import no_mutations


__all__ = [
    MutationError,
    no_mutations
]