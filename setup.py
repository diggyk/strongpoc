#!/usr/bin/env python

import os
import sys
from subprocess import check_output

from distutils import log
from distutils.core import Command

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from setuptools.command.develop import develop as DevelopCommand
from setuptools.command.sdist import sdist as SDistCommand

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

execfile('dev/strongpoc/version.py')

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        log.info('Running python tests...')
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


class DevelopWithBuildStatic(DevelopCommand):
    def install_for_development(self):
        self.run_command('build_static')
        return DevelopCommand.install_for_development(self)


class SDistWithBuildStatic(SDistCommand):
    def run(self):
        self.run_command('build_static')
        SDistCommand.run(self)


class BuildStatic(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        log.info('running [npm install --quiet]')
        check_output(['npm', 'install', '--quiet'], cwd=ROOT)

        log.info('running [gulp clean]')
        check_output([os.path.join(ROOT, 'node_modules', '.bin', 'gulp'), 'clean'], cwd=ROOT)

        log.info('running [gulp build]')
        check_output([os.path.join(ROOT, 'node_modules', '.bin', 'gulp'), 'build'], cwd=ROOT)


kwargs = {
    'name': 'strongpoc',
    'version': str(__version__),
    'packages': find_packages(exclude=['tests*']),
    'include_package_data': True,
    'description': 'Strong Point of Contact (Team contact management)',
    'author': 'Digant C Kasundra',
    'maintainer': 'Digant C Kasundra',
    'author_email': 'digant@dropbox.com',
    'maintainer_email': 'digant@dropbox.com',
    'license': 'Apache',
    'install_requires': required,
    'url': 'https://github.com/dropbox/strongpoc',
    'tests_require': ['pytest'],
    'cmdclass': {
        'test': PyTest,
        'build_static': BuildStatic,
        'develop': DevelopWithBuildStatic,
        'sdist': SDistWithBuildStatic,
    },
    'entry_points': """
        [console_scripts]
        nsot-server=nsot.util:main
    """,
    'classifiers': [
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
}

setup(**kwargs)
