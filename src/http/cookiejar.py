from __future__ import absolute_import
import sys

assert sys.version_info[0] < 3

# REVIEW: cookielib renamed to http.cookiejar in Python 3.
from cookielib import *
