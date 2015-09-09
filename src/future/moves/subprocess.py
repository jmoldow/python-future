from __future__ import absolute_import
from future.utils import PY2, PY26

from subprocess import *

if PY2:
    __future_module__ = True
    # REVIEW: Backport getoutput, getstatusoutput functions from Python 3.
    from commands import getoutput, getstatusoutput

if PY26:
    # REVIEW: Backport check_output function from Python 2.7+.
    from future.backports.misc import check_output
