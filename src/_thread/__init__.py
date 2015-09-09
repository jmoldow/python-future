from __future__ import absolute_import
import sys
__future_module__ = True

# REVIEW: thread renamed to _thread in Python 3.
if sys.version_info[0] < 3:
    from thread import *
else:
    raise ImportError('This package should not be accessible on Python 3. '
                      'Either you are trying to run from the python-future src folder '
                      'or your installation of python-future is corrupted.')
