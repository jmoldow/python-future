from __future__ import absolute_import
from future.utils import PY3

if not PY3:
    __future_module__ = True

# REVIEW: This module shouldn't exist (unless the author is intentionally
# making an API for accessing a moved but non-backported version of urllib). In
# install_aliases(), the backported, not moved, versions are used.
