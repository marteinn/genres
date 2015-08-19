#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pip

import genres
from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

# Handle requirements
requires = parse_requirements("requirements/tests.txt",
                              session=pip.download.PipSession())
tests_require = [str(ir.req) for ir in requires]

packages = [
    "genres"
]

requires = []

# Convert markdown to rst
try:
    from pypandoc import convert
    long_description = convert("README.md", "rst")
except:
    long_description = ""


setup(
    name="genres",
    version=genres.__version__,
    description="Determine musical genres for text with musical context "
                "(such as reviews)",
    long_description=long_description,
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/genres",
    packages=packages,
    package_data={"": ["LICENSE", "reviews.txt"], "genres": ["*.txt"]},
    package_dir={"genres": "genres"},
    include_package_data=True,
    install_requires=requires,
    tests_require=tests_require,
    license="MIT",
    zip_safe=False,
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4"
    ),
    extras_require={
    },
)
