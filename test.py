#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests"""

import re
import os
import unittest
from genres import find


class GenreTestCase(unittest.TestCase):
    def test_single_match(self):
        result = find("This is a good example of techno. Hello techno.")
        assert "techno" in result

    def test_multiple_match(self):
        result = find("This is Dance Hall. Sounds like a mix of Merengue")
        assert "dance hall" in result

    def multiple_and_invalid(self):
        result = find("KingstonDance Hall and Reggae")
        assert "dance hall" not in result

    def test_conflicting_genres(self):
        result = find("Dance Hall and Reggae-Techno")
        assert "techno" not in result

    def test_not_existing_genre(self):
        result = find("Lorem ipsum dolum test")
        assert len(result) == 0

    def test_highest_occurence_return_genre(self):
        result = find("ska, Techno, Ska")
        assert "ska" in result

    def test_comment_data(self):
        result = find("#comment")
        assert "#comment" not in result

    def test_tag_match(self):
        result = find("In this text we have a Country Test Tag")
        assert "country" in result

    def test_escaped_genre(self):
        result = find("For over a decade, Los Angeles singer/songwriter \
            Jhené Aiko has skirted the periphery of R&B stardom")
        assert "r&b" in result

    def test_between_words(self):
        result = find("Hip-hop is a genre")
        assert "hip hop" in result


class TestTagCase(unittest.TestCase):
    def test_genre_tag_occurence(self):
        result = find("Ska jazz. Ska jazz. The best jazz player is Miles Davis. \
        Miles Davis. Miles Davis")
        assert "ska jazz" == result[0]

    def test_tag_vs_genre_check(self):
        result = find("Miles Davis. Miles Davis. Miles Davis. Techno. Techno.")
        assert "jazz" in result
        assert len(result) == 1


class TestArticleContentCase(unittest.TestCase):
    reviews = []

    def setUp(self):
        data_path = "%s/reviews.txt" % os.path.dirname(
                os.path.abspath(__file__))

        with open(data_path, "r") as data_file:
            raw_data = data_file.read()

        data_file.close()
        raw_data = raw_data.strip()

        reviews = raw_data.split("\n")
        for review in reviews:
            review = review.strip()

            if len(review) == 0:
                continue

            if review[:1].startswith("#"):
                continue

            review_struct = review.split(";")
            category = review_struct[0].split(",")
            content = "".join(review_struct[1:])

            self.reviews.append([category, content])

    def tearDown(self):
        pass

    def test_reviews(self):
        for review in self.reviews:
            result = find(review[1])
            found = all((w in result for w in review[0]))
            if not found:
                raise AssertionError("%s Genres %s not found in %s",
                    review[1][:20], review[0], result)

if __name__ == "__main__":
    unittest.main()
