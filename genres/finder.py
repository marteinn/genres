# -*- coding: utf-8 -*-

"""
genres.finder
---

This module handles the genre finder.
"""

from collections import Counter
import re


class Finder():
    db = None
    unique_category = True

    def __init__(self, db, unique_category=True):
        self.db = db
        self.unique_category = unique_category

    def find(self, text):
        """
        Return a list of genres found in text.
        """

        genres = []
        text = text.lower()

        category_counter = Counter()
        counter = Counter()

        for genre in self.db.genres:
            found = self.contains_entity(genre, text)
            if found:
                counter[genre] += found

                category = self.db.reference[genre]
                points = self.db.points[genre]
                points *= found

                # Add bonus points if additional terms points to category
                if category_counter[category] > 0:
                    points += 1

                category_counter[category] += points

        for tag in self.db.tags:
            found = self.contains_entity(tag, text)
            if found:
                category = self.db.reference[tag]

                if not counter[category]:
                    counter[category] += found

                points = self.db.points[tag]
                points *= found
                category_counter[category] += points

        if not category_counter:
            return genres

        main_category = category_counter.most_common(1)[0][0]

        # Convert counter to a flat list of genres, sorted by count
        sorted_genres = [ite for ite, it in counter.most_common()]

        for genre in sorted_genres:
            insert = True

            if self.unique_category:
                if not self.db.reference[genre] == main_category:
                    insert = False

            if insert:
                genres.append(genre)

        return genres

    @staticmethod
    def contains_entity(entity, text):
        """
        Attempt to try entity, return false if not found. Otherwise the
        amount of time entitu is occuring.
        """

        try:
            entity = re.escape(entity)
            entity = entity.replace("\ ", "([^\w])?")
            pattern = "(\ |-|\\\|/|\.|,|^)%s(\ |\-|\\\|/|\.|,|$)" % entity
            found = len(re.findall(pattern, text, re.I | re.M))
        except Exception as e:
            found = False

        return found
