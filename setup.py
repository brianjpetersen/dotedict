# standard libraries
import setuptools
# third party libraries
pass
# first party libraries
pass

try:
    with open('README.md') as f:
        readme = f.read()
except:
    readme = None

try:
    with open('VERSION.md') as f:
        version = f.read()
except:
    version = None

setuptools.setup(
    name = 'dotedict',
    version = version,
    description = readme,
    author = 'Brian Petersen',
    author_email = 'brianjpetersen@gmail.com',
)