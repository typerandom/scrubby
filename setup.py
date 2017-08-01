'''
Handles packaging, distribution, and testing.
'''

from sys import exit
from subprocess import call
from setuptools import Command, find_packages, setup

class BaseCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

class TestCommand(BaseCommand):
    description = 'run tests'

    def run(self):
        exit(call(['py.test', '--quiet']))

class ReleaseCommand(BaseCommand):
    description = 'Cut a new PyPI release.'

    def run(self):
        call(['rm', '-rf', 'build', 'dist'])
        ret = call(['python', 'setup.py', 'sdist', 'bdist_wheel', '--universal', 'upload'])
        exit(ret)

setup(
    # Basic package information.
    name = 'scrubby',
    version = '0.1.13',
    packages = find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),

    # Packaging options.
    zip_safe = False,
    include_package_data = True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'scrubby = scrubby.cli:main',
        ],
    },

    # Package dependencies.
    install_requires = ['pyyaml==3.12'],
    extras_require = {
        'test': ['pytest', 'pytest-cov'],
    },
    cmdclass = {
        'test': TestCommand,
        'release': ReleaseCommand,
    },

    # Metadata for PyPI.
    author = 'Robin Orheden',
    author_email = 'orhedenr@gmail.com',
    license = 'LICENSE.md',
    url = 'http://github.com/typerandom/scrubby',
    keywords = 'data scrubbing',
    description = 'Let Scrubby clean your datasource.',
    long_description = open('README.md').read()

)