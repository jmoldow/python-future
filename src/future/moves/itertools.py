from __future__ import absolute_import

from itertools import *
# REVIEW: i* functions renamed without leading i in Python 3.
# REVIEW: The renamed not present here (map, filter, etc.) are actually done in
# the standard library. map, filter, etc. are not in itertools in Python 3.
try:
    zip_longest = izip_longest
    filterfalse = ifilterfalse
except NameError:
    pass
