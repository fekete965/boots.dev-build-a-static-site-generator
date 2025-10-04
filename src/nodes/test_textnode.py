import unittest

from .textnode import TextNode
from .texttype import TextType


class TestTextNode(unittest.TestCase):
    def test_eq_without_url(self):
        node = TextNode(
            text="This is a text node",
            type=TextType.BOLD,
        )
        node2 = TextNode(
            text="This is a text node",
            type=TextType.BOLD,
        )

        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode(
            text="This is a text node",
            type=TextType.BOLD,
            url="https://www.boot.dev",
        )
        node2 = TextNode(
            text="This is a text node",
            type=TextType.BOLD,
            url="https://www.boot.dev",
        )

        self.assertEqual(node, node2)

    def test_different_type(self):
        node = TextNode(
            text="This is a text node",
            type=TextType.ITALIC,
        )
        node2 = TextNode(
            text="This is a text node",
            type=TextType.BOLD,
        )

        self.assertNotEqual(node, node2)

    def test_different_text(self):
        node = TextNode(
            text="This is a banana",
            type=TextType.ITALIC,
        )
        node2 = TextNode(
            text="Hello, there!",
            type=TextType.ITALIC,
        )

        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode(
            text="This is a banana",
            type=TextType.ITALIC,
            url=None,
        )
        node2 = TextNode(
            text="Hello, there!",
            type=TextType.ITALIC,
            url="https://www.boot.dev",
        )

        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
