from __future__ import absolute_import
from future.utils import PY3

# REVIEW: htmlentitydefs renamed to html.entities in Python 3.
if PY3:
    from html.entities import *
else:
    from future.moves.html.entities import *
