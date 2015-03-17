# standard libraries
import setuptools
# third party libraries
pass
# first party libraries
pass

<<<<<<< HEAD
def load_file(fname):
    try:
        with open(fname, 'rb') as f:
            d = f.read()
    except:
        d = None
    return d

readme = load_file('README.md')
version = load_file('VERSION.md')
license = load_file('LICENSE.md')

setuptools.setup(
    name = 'tiny_id',
    version = version,
=======
try:
    with open('README.md') as f:
        readme = f.read()
except:
    readme = None

setuptools.setup(
    name = 'dotedict',
    version = '0.0.1',
>>>>>>> parent of 763f213... Up revision, with slight refactoring for improved versioning and
    description = readme,
    license = license,
    author = 'Brian Petersen',
    author_email = 'brianjpetersen@gmail.com',
)