import unittest

from textNodeToHtmlNode import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node_raw_text(self):
        text_node = TextNode(type=TextType.TEXT, text="Hello, there!")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello, there!")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode(type=TextType.ITALIC, text="Italic hello, there!")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "Italic hello, there!")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode(type=TextType.BOLD, text="Bold hello, there!")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "Bold hello, there!")

    def test_text_node_to_html_node_code(self):
        text_node = TextNode(type=TextType.CODE, text="Code hello, there!")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "Code hello, there!")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode(
            type=TextType.LINK, text="Link hello, there!", url="https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "Link hello, there!")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_text_node_to_html_node_image(self):
        text_node = TextNode(
            type=TextType.IMAGE, text="Image hello, there!", url="https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "Image hello, there!")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev"})
