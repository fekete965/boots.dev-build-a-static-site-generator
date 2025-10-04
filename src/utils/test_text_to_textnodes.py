import unittest

from src.nodes.texttype import TextType
from .text_to_textnodes import text_to_text_nodes


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes_raw_text(self):
        text = "Hello, there!"
        nodes = text_to_text_nodes(text)

        self.assertEqual(len(nodes), 1)

        self.assertEqual(nodes[0].type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "Hello, there!")
        self.assertEqual(nodes[0].url, None)

    def test_text_to_text_nodes_italic(self):
        text = "This is a _italic_ text"
        nodes = text_to_text_nodes(text)

        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].url, None)

        self.assertEqual(nodes[1].type, TextType.ITALIC)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].url, None)

    def test_text_to_text_nodes_bold(self):
        text = "This is a *bold* text"
        nodes = text_to_text_nodes(text)

        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].url, None)

        self.assertEqual(nodes[1].type, TextType.BOLD)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[2].url, None)

    def test_text_to_text_nodes_code(self):
        text = "This is a `code` text"
        nodes = text_to_text_nodes(text)

        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].url, None)

        self.assertEqual(nodes[1].type, TextType.CODE)
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].url, None)

    def test_text_to_text_nodes_image(self):
        text = "This is a ![image](https://www.boot.dev) text"
        nodes = text_to_text_nodes(text)

        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].url, None)

        self.assertEqual(nodes[1].type, TextType.IMAGE)
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].url, "https://www.boot.dev")

    def test_text_to_text_nodes_link(self):
        text = "This is a [link](https://www.boot.dev) text"
        nodes = text_to_text_nodes(text)

        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].url, None)

        self.assertEqual(nodes[1].type, TextType.LINK)
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].url, "https://www.boot.dev")

        self.assertEqual(nodes[2].type, TextType.TEXT)
        self.assertEqual(nodes[2].text, " text")
        self.assertEqual(nodes[2].url, None)

    def test_text_to_text_nodes_complex_scenario(self):
        text = "This is a *bold* _italic_ `code` text. Also check out this image ![image](https://www.super-image.co.uk) and this link [link](https://www.boot.dev). These resources are truly amazing!"
        nodes = text_to_text_nodes(text)

        self.assertEqual(len(nodes), 11)

        self.assertEqual(nodes[0].type, TextType.TEXT)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].url, None)

        self.assertEqual(nodes[1].type, TextType.BOLD)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].url, None)

        self.assertEqual(nodes[2].type, TextType.TEXT)
        self.assertEqual(nodes[2].text, " ")
        self.assertEqual(nodes[2].url, None)

        self.assertEqual(nodes[3].type, TextType.ITALIC)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].url, None)

        self.assertEqual(nodes[4].type, TextType.TEXT)
        self.assertEqual(nodes[4].text, " ")
        self.assertEqual(nodes[4].url, None)

        self.assertEqual(nodes[5].type, TextType.CODE)
        self.assertEqual(nodes[5].text, "code")
        self.assertEqual(nodes[5].url, None)

        self.assertEqual(nodes[6].type, TextType.TEXT)
        self.assertEqual(nodes[6].text, " text. Also check out this image ")
        self.assertEqual(nodes[6].url, None)

        self.assertEqual(nodes[7].type, TextType.IMAGE)
        self.assertEqual(nodes[7].text, "image")
        self.assertEqual(nodes[7].url, "https://www.super-image.co.uk")

        self.assertEqual(nodes[8].type, TextType.TEXT)
        self.assertEqual(nodes[8].text, " and this link ")
        self.assertEqual(nodes[8].url, None)

        self.assertEqual(nodes[9].type, TextType.LINK)
        self.assertEqual(nodes[9].text, "link")
        self.assertEqual(nodes[9].url, "https://www.boot.dev")

        self.assertEqual(nodes[10].type, TextType.TEXT)
        self.assertEqual(
            nodes[10].text, ". These resources are truly amazing!")
        self.assertEqual(nodes[10].url, None)
