# standard libraries
import setuptools
# third party libraries
pass
# first party libraries
pass

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
    description = readme,
    license = license,
    author = 'Brian Petersen',
    author_email = 'brianjpetersen@gmail.com',
)