from __future__ import absolute_import

from future.utils import PY2

from sys import *

# REVIEW: __builtin__.intern moved to sys package in Python 3.
if PY2:
    from __builtin__ import intern
