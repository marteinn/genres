#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import genres
from pypandoc import convert

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

packages = [
    "genres"
]

requires = []

# Convert markdown to rst
long_description = convert("README.md", "rst")


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
    license="MIT",
    zip_safe=False,
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"
    ),
    extras_require={
    },
)
