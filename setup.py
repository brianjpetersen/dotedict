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

setuptools.setup(
    name = 'dotedict',
    version = '0.0.1',
    description = readme,
    author = 'Brian Petersen',
    author_email = 'brianjpetersen@gmail.com',
)