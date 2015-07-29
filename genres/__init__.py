# -*- coding: utf-8 -*-

"""
genres
---

Genres is a library that analyzes text with musical context and guesses genres.

    >>> import genres
    >>> r = genres.find("Pink Floyd is a great rock band")
    >>> r
    >>> ["Rock"]

:copyright: (c) 2014 by Martin Sandström
:license: MIT, see LICENSE for more details.
"""

__title__ = "genres"
__version__ = "1.1.1"
__build__ = 111
__author__ = "Martin Sandström"
__license__ = "MIT"
__copyright__ = "Copyright 2014-2015 Martin Sandström"


from .api import find  # NOQA
