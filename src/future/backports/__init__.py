# future.backports package
from __future__ import absolute_import
import sys
__future_module__ = True
from future.standard_library import import_top_level_modules

if sys.version_info[0] == 3:
    import_top_level_modules()

# REVIEW: This, and future.backports.urllib, are the only things exported from
# here by default. Everything else is an "alpha-quality backport of new/changed
# functionality from Python 3".  You can access them manually, or you can use
# the import_() / import_from() helpers in future.standard_library. Otherwise,
# they won't be used.
from .misc import (ceil,
                   OrderedDict,
                   Counter,
                   ChainMap,
                   check_output,
                   count,
                   recursive_repr,
                   _count_elements,
                  )
