# -*- coding: utf-8 -*-

"""
genres.api
---

This module implements the Genres API.
"""

import logging
from . import finder, db

_db = None


def find(text):
    """
    Tries to determine genres for the text.
    """

    finder_obj = _create_finder()
    return finder_obj.find(text)


def _get_database():
    """
    Check if database has been created, otherwise construct it.
    """

    global _db
    if not _db:
        db_obj = db.Db()
        _db = db_obj

    return _db


def _create_finder():
    """
    Create finder object based on db.
    """

    db_obj = _get_database()
    return finder.Finder(db_obj)
