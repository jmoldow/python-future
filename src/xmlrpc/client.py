from __future__ import absolute_import
import sys

assert sys.version_info[0] < 3
# REVIEW: xmlrpclib renamed to xmlrpc.client in Python 3.
from xmlrpclib import *
