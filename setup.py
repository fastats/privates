#!/usr/bin/env python3

import importlib.util
from os import path

from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

# import just the _version module, don't pull in any dependencies
spec = importlib.util.spec_from_file_location(
    '_version', path.join(here, 'privates', '_version.py')
)
version_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version_module)

version = version_module.VERSION


setup_kwargs = dict(
    name='fastats-privates',
    version=version,
    description='A python library using private/hidden python language features',
    url='https://github.com/fastats/privates',
    author='Fastats Developers',
    author_email='fastats@googlegroups.com',

    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',

        'Operating System :: OS Independent',

        'License :: Freely Distributable',
        'License :: Freeware',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='python helpers utils internals',
    packages=find_packages(exclude=['tests', 'tests.*']),

    setup_requires=[
        'pytest-runner',    # to enable pytest for setup.py test via setup.cfg
    ],

    install_requires=[
        'numba>=0.37.0',
    ],

    tests_require=[
        'pytest',
        'pytest-cov',
        'setuptools',   # for pkg_resources
    ],

    extras_require={
        'doc': [    # documentation
            'sphinx',
            'sphinx_rtd_theme',
        ],
    },
)


# CI-specific test utilities, e.g. travis, appveyor
setup_kwargs['extras_require']['ci_test'] = (
    setup_kwargs['tests_require']
    + [
        'codecov',
        'httpie',
    ]
)

# All ("development") requirements, including docs generation and tests,
# but no CI-specific ones
setup_kwargs['extras_require']['dev'] = (
    setup_kwargs['tests_require']
    + setup_kwargs['extras_require']['doc']
)


setup(**setup_kwargs)
