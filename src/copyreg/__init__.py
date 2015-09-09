from __future__ import absolute_import
import sys

# REVIEW: Renamed from copy_reg to copyreg in Python 3.
if sys.version_info[0] < 3:
    from copy_reg import *
else:
    raise ImportError('This package should not be accessible on Python 3. '
                      'Either you are trying to run from the python-future src folder '
                      'or your installation of python-future is corrupted.')
