import unittest

from .leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_without_props(self):
        node = LeafNode(tag="h1", value="Hello, there!", props=None)
        self.assertEqual(node.to_html(), "<h1>Hello, there!</h1>")

    def test_to_html_with_props(self):
        node = LeafNode(
            tag="a",
            value="Click me, mortal!",
            props={"class": "text-2xl font-bold", "href": "https://www.boot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            '<a class="text-2xl font-bold" href="https://www.boot.dev">Click me, mortal!</a>',
        )
