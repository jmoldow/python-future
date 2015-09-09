from __future__ import absolute_import
from future.utils import PY3

# REVIEW: robotparser renamed to urllib.robotparser in Python 3.
if PY3:
    from urllib.robotparser import *
else:
    __future_module__ = True
    from robotparser import *
