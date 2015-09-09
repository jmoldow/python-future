from __future__ import absolute_import
import sys

from future.utils import PY2, PY26
__future_module__ = True

from collections import *

# REVIEW: User* classes moved to collections in Python 3.
if PY2:
    from UserDict import UserDict
    from UserList import UserList
    from UserString import UserString

# REVIEW: Backported OrderedDict, Counter from Python 3.
if PY26:
    from future.backports.misc import OrderedDict, Counter

# REVIEW: Backported ChainMap from Python 3.
if sys.version_info < (3, 3):
    from future.backports.misc import ChainMap, _count_elements
