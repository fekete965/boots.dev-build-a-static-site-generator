import unittest

from .extract_markdown_images import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_no_images(self):
        text = "Hello, there!"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_extract_markdown_images_single_link(self):
        text = "![Hello, there!](https://www.boot.dev)"
        images = extract_markdown_images(text)

        self.assertEqual(images, [("Hello, there!", "https://www.boot.dev")])

    def test_extract_markdown_images_multiple_images(self):
        text = "![Hello, there!](https://www.boot.dev) ![Google meh](https://www.google.com)"
        images = extract_markdown_images(text)

        self.assertEqual(
            images,
            [
                ("Hello, there!", "https://www.boot.dev"),
                ("Google meh", "https://www.google.com")
            ]
        )
