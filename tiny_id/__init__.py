# standard libraries
pass
# third party libraries
pass
# first party libraries
<<<<<<< HEAD:tiny_id/__init__.py
from tiny_id import random

_FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(_FILE_DIRECTORY, '..', 'VERSION.md'), 'rb') as f:
        __version__ = f.read()
except:
    pass
=======
from dotedict import DoteDict
>>>>>>> parent of 763f213... Up revision, with slight refactoring for improved versioning and:dotedict/__init__.py
