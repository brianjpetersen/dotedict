# standard libraries
import os
import setuptools
# third party libraries
pass
# first party libraries
pass

project_name = 'dotedict'
author = 'Brian J Petersen'
author_email = None

def load_file(fname, default=None):
    try:
        with open(fname, 'rb') as f:
            d = f.read()
    except:
        d = default
    return d

readme = load_file('README.md', '')
history = load_file('HISTORY.md', '')
version = load_file('VERSION', None)
license = load_file('LICENSE', None)
roadmap = load_file('TODO.md', '')

assert project_name is not ValueError, 'Please name your project.'
assert author is not ValueError, 'Please define the author\'s name.'

if version is None:
    package_data = {}
else:
    package_data = {project_name: ['../VERSION', ]}

setuptools.setup(
    name = project_name,
    version = version,
    description = readme,
    long_description = readme + '\n\n' + history + '\n\n' + roadmap,
    license = license,
    author = author,
    author_email = author_email,
    packages = setuptools.find_packages(),
    package_data = package_data,
)