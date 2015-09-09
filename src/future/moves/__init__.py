# future.moves package
from __future__ import absolute_import
import sys
__future_module__ = True
from future.standard_library import import_top_level_modules

if sys.version_info[0] == 3:
    import_top_level_modules()

# REVIEW: Renamed top-level modules are installed at their Python 3 locations,
# and are also available at future.moves.
# REVIEW: Refactored packages / backported features are moved to their Python 3
# locations by future.standard_library.install_aliases(), and are also
# available at future.moves.
