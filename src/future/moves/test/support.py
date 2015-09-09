from __future__ import absolute_import
from future.standard_library import suspend_hooks
from future.utils import PY3

# REVIEW: test.support renamed to test.test_support in Python 3.
if PY3:
    from test.support import *
else:
    __future_module__ = True
    # REVIEW: suspend_hooks() necessary when importing names from old top-level
    # module into new top-level module with the same name. Need to make sure to
    # import from the old, not the new.
    with suspend_hooks():
        from test.test_support import *

