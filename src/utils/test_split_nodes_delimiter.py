import unittest

from src.nodes.textnode import TextNode
from src.nodes.texttype import TextType
from .split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_with_invalid_markdown_syntax(self):
        node = TextNode(
            text="_I am utterly alone",
            type=TextType.TEXT,
        )

        try:
            split_nodes_delimiter([node], "_", TextType.ITALIC)
        except Exception as e:
            self.assertEqual(str(e), "Invalid Markdown syntax")

    def test_split_nodes_delimiter_with_single_chunk(self):
        node = TextNode(
            text="_I am utterly alone_",
            type=TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter(
            old_nodes=[node],
            delimiter="_",
            text_type=TextType.ITALIC,
        )
        self.assertEqual(len(new_nodes), 1)

        self.assertEqual(new_nodes[0].type, TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "I am utterly alone")

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
