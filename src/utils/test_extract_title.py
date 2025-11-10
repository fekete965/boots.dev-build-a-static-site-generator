import unittest

from .extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_no_title(self):
        markdown_str = "Hello, there!"

        try:
            extract_title(markdown_str)
        except Exception as e:
            self.assertEqual(str(e), "No title found in markdown")

        markdown_str = "Hello, there!\nWith a longer text.\n And multiple lines"

        try:
            extract_title(markdown_str)
        except Exception as e:
            self.assertEqual(str(e), "No title found in markdown")

    def test_extract_title_single_title(self):
        markdown_str = "# Hello, there!"
        title = extract_title(markdown_str)
        self.assertEqual(title, "Hello, there!")

    def test_extract_title_multiple_titles(self):
        markdown_str = "# Hello, there!\n# Goodbye, there!"
        title = extract_title(markdown_str)
        self.assertEqual(title, "Hello, there!")
