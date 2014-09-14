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

    @staticmethod
    def contains_entity(entity, text):
        try:
            entity = re.escape(entity)
            entity = entity.replace("\ ", "([^\w])?")
            found = re.search("(\ |-|\|/|\.|,|^)%s(\ |\-|\|/|\.|,|$)" % entity,
                text, re.I | re.M)
        except Exception, e:
            found = False

        return found

    def find(self, text):
        genres = []
        text = text.lower()

        category_counter = Counter()
        counter = Counter()

        for genre in self.db.genres:
            if self.contains_entity(genre, text):
                counter[genre] += 1
                category = self.db.reference[genre]
                category_counter[category] += 1

        for tag in self.db.tags:
            if self.contains_entity(tag, text):
                category = self.db.reference[tag]

                # Only increase main category count once when tag is found.
                if not counter[category]:
                    counter[category] += 1

                category_counter[category] += 1

        if len(category_counter) == 0:
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
