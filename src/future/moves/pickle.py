from __future__ import absolute_import
from future.utils import PY3

# REVIEW: If on Python 2 and the faster cPickle package is available, use it
# and shadow the slower pickle package.
if PY3:
    from pickle import *
else:
    __future_module__ = True
    try:
        from cPickle import *
    except ImportError:
        from pickle import *
