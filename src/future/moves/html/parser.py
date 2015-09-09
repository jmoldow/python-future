from __future__ import absolute_import
from future.utils import PY3
__future_module__ = True

# REVIEW: HTMLParser renamed to html.parser in Python 3.
if PY3:
    from html.parser import *
else:
    from HTMLParser import *
