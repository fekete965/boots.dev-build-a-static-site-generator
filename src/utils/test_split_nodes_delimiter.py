import unittest

from nodes.textnode import TextNode, TextType
from .split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_italic(self):
        node = TextNode(
            text="This is simple text with a _italic_ word",
            type=TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(len(new_nodes), 3)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "This is simple text with a ")

        self.assertEqual(new_nodes[1].type, TextType.ITALIC)
        self.assertEqual(new_nodes[1].text, "italic")

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " word")

    def test_split_nodes_delimiter_bold(self):
        node = TextNode(
            text="This is simple text with a **bold** word",
            type=TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 3)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "This is simple text with a ")

        self.assertEqual(new_nodes[1].type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "bold")

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " word")

    def test_split_nodes_delimiter_code(self):
        node = TextNode(
            text="This is simple text with a `code` word",
            type=TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "This is simple text with a ")

        self.assertEqual(new_nodes[1].type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code")

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " word")
