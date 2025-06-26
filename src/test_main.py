import unittest
import os
import sys

from util import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_valid_h1_title_with_space(self):
        self.assertEqual(extract_title("# My Awesome Title"), "My Awesome Title")

    def test_valid_h1_title_without_space_after_hash(self):
        # Current implementation removes all leading '#' and then strips spaces.
        self.assertEqual(extract_title("#MyTitle"), "MyTitle")

    def test_valid_h1_title_with_multiple_leading_hashes(self):
        # Current implementation removes all leading '#' and then strips spaces.
        self.assertEqual(extract_title("### My Multi-Hash Title"), "My Multi-Hash Title")

    def test_valid_h1_title_with_extra_leading_spaces_after_hash(self):
        self.assertEqual(extract_title("#  Title With Extra Spaces"), "Title With Extra Spaces")

    def test_valid_h1_title_with_trailing_spaces(self):
        self.assertEqual(extract_title("# Title with trailing spaces   "), "Title with trailing spaces")

    def test_valid_h1_title_with_leading_and_trailing_spaces(self):
        self.assertEqual(extract_title("#  Title with leading and trailing spaces   "), "Title with leading and trailing spaces")

    def test_invalid_title_no_hash(self):
        with self.assertRaises(ValueError) as cm:
            extract_title("This is not a title")
        self.assertEqual(str(cm.exception), "Invlaid title, should start with '#'.")

    def test_invalid_title_empty_string(self):
        with self.assertRaises(ValueError) as cm:
            extract_title("")
        self.assertEqual(str(cm.exception), "Invlaid title, should start with '#'.")

    def test_invalid_title_hash_not_at_beginning(self):
        with self.assertRaises(ValueError) as cm:
            extract_title("Some text # My Title")
        self.assertEqual(str(cm.exception), "Invlaid title, should start with '#'.")