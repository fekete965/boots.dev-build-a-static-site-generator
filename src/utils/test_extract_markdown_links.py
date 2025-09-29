import unittest

from .extract_markdown_links import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links_no_links(self):
        text = "Hello, there!"
        links = extract_markdown_links(text)
        self.assertEqual(links, [])

    def test_extract_markdown_links_single_link(self):
        text = "[Hello, there!](https://www.boot.dev)"
        links = extract_markdown_links(text)

        self.assertEqual(links, [("Hello, there!", "https://www.boot.dev")])

    def test_extract_markdown_links_multiple_links(self):
        text = "[Hello, there!](https://www.boot.dev) [Google meh](https://www.google.com)"
        links = extract_markdown_links(text)

        self.assertEqual(
            links,
            [
                ("Hello, there!", "https://www.boot.dev"),
                ("Google meh", "https://www.google.com")
            ]
        )
