# -*- coding: utf-8 -*-

"""
genres.db
---

This module handles the genres database.
"""

import os


class Db:
    reference = None
    genres = None
    tags = None

    def __init__(self, data_path=None):
        if not data_path:
            data_path = "%s/data.txt" % os.path.dirname(
                os.path.abspath(__file__))

        data = self.load(data_path)
        self.parse(data)

    def load(self, data_path):
        with open(data_path, "r") as data_file:
            raw_data = data_file.read()

        data_file.close()
        return raw_data

    def parse(self, data):
        categories = data.split("\n\n")
        reference = {}
        genre_index = []
        tag_index = []

        for category in categories:
            entries = category.strip().split("\n")
            entry_category = entries[0].lower()
            for entry in entries:
                entry = entry.lower()
                if not entry:
                    continue

                # Comment, ignore
                if entry.startswith("#"):
                    continue

                # Handle genre
                if not entry.startswith("-"):
                    genre = entry

                    reference[genre] = entry_category
                    genre_index.append(genre)

                # Handle tag
                else:
                    tag = entry[1:]
                    tag = tag.strip()

                    reference[tag] = entry_category
                    tag_index.append(tag)

        self.reference = reference
        self.genres = genre_index
        self.tags = tag_index
