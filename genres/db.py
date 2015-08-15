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
    points = None

    def __init__(self, data_path=None):
        if not data_path:
            data_path = "%s/data.txt" % os.path.dirname(
                os.path.abspath(__file__))

        data = self.load(data_path)
        self.parse(data)

    @staticmethod
    def load(data_path):
        """
        Extract data from provided file and return it as a string.
        """
        with open(data_path, "r") as data_file:
            raw_data = data_file.read()

        data_file.close()
        return raw_data

    def parse(self, data):
        """
        Split and iterate through the datafile to extract genres, tags
        and points.
        """

        categories = data.split("\n\n")
        reference = {}
        reference_points = {}
        genre_index = []
        tag_index = []

        for category in categories:
            entries = category.strip().split("\n")
            entry_category, entry_points = self._parse_entry(entries[0].lower())

            if entry_category.startswith("#"):
                continue

            for entry in entries:
                entry = entry.lower()
                if not entry:
                    continue

                # Comment, ignore
                if entry.startswith("#"):
                    continue

                # Handle genre
                if not entry.startswith("-"):
                    genre, points = self._parse_entry(entry)

                    reference[genre] = entry_category
                    reference_points[genre] = points
                    genre_index.append(genre)

                # Handle tag
                else:
                    tag = entry[1:]
                    tag, points = self._parse_entry(tag, limit=9.5)

                    reference[tag] = entry_category
                    reference_points[tag] = points
                    tag_index.append(tag)

        self.reference = reference
        self.genres = genre_index
        self.tags = tag_index
        self.points = reference_points

    @staticmethod
    def _parse_entry(entry, limit=10):
        """
        Finds both label and if provided, the points for ranking.
        """

        entry = entry.split(",")
        label = entry[0]
        points = limit

        if len(entry) > 1:
            proc = float(entry[1].strip())
            points = limit * proc

        return label, int(points)
