# standard libraries
import os
# third party libraries
pass
# first party libraries
from tiny_id import random

_FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(_FILE_DIRECTORY, '..', 'VERSION.md'), 'rb') as f:
        __version__ = f.read()
except:
    pass