import unittest

from src.nodes.textnode import TextNode, TextType
from .split_nodes_image import split_nodes_image


class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image_no_images_single_node(self):
        nodes = [TextNode(text="Hello, there!", type=TextType.TEXT)]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(len(new_nodes), 1)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Hello, there!')
        self.assertEqual(new_nodes[0].url, None)

    def test_split_nodes_image_no_images_multiple_nodes(self):
        nodes = [
            TextNode(text="Hello, there!", type=TextType.TEXT),
            TextNode(text="Ahoy, matey!", type=TextType.TEXT),
            TextNode(text="Howdy, partner!", type=TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(len(new_nodes), 3)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Hello, there!')
        self.assertEqual(new_nodes[0].url, None)

        self.assertEqual(new_nodes[1].type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, 'Ahoy, matey!')
        self.assertEqual(new_nodes[1].url, None)

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, 'Howdy, partner!')
        self.assertEqual(new_nodes[2].url, None)

    def test_split_nodes_image_with_single_image_node(self):
        nodes = [
            TextNode(
                text="![Hello, there!](https://www.boot.dev)",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(len(new_nodes), 1)

        self.assertEqual(new_nodes[0].type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].text, 'Hello, there!')
        self.assertEqual(new_nodes[0].url, 'https://www.boot.dev')

    def test_split_nodes_image_with_multiple_image_nodes(self):
        nodes = [
            TextNode(
                text="![Hello, there!](https://www.boot.dev)",
                type=TextType.TEXT,
            ),
            TextNode(
                text="![Google meh](https://www.google.com)",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(len(new_nodes), 2)

        self.assertEqual(new_nodes[0].type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].text, 'Hello, there!')
        self.assertEqual(new_nodes[0].url, 'https://www.boot.dev')

        self.assertEqual(new_nodes[1].type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].text, 'Google meh')
        self.assertEqual(new_nodes[1].url, 'https://www.google.com')

    def test_split_nodes_image_with_single_node_that_contains_a_single_image_at_the_end_of_the_text(self):
        nodes = [
            TextNode(
                text="Oh wow, look at this: ![Hello, there!](https://www.boot.dev)",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(len(new_nodes), 2)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Oh wow, look at this: ')
        self.assertEqual(new_nodes[0].url, None)

        self.assertEqual(new_nodes[1].type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].text, 'Hello, there!')
        self.assertEqual(new_nodes[1].url, 'https://www.boot.dev')

    def test_split_nodes_image_with_single_node_that_contains_a_single_image_at_the_beginning_of_the_text(self):
        nodes = [
            TextNode(
                text="![Hello, there!](https://www.boot.dev) <- this is interesting",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(len(new_nodes), 2)

        self.assertEqual(new_nodes[0].type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].text, 'Hello, there!')
        self.assertEqual(new_nodes[0].url, 'https://www.boot.dev')

        self.assertEqual(new_nodes[1].type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, ' <- this is interesting')
        self.assertEqual(new_nodes[1].url, None)

    def test_split_nodes_image_with_single_node_that_contains_a_single_image_in_the_middle_of_the_text(self):
        nodes = [
            TextNode(
                text="Oh wow, look at this: ![Hello, there!](https://www.boot.dev) <- this is interesting",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(len(new_nodes), 3)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Oh wow, look at this: ')
        self.assertEqual(new_nodes[0].url, None)

        self.assertEqual(new_nodes[1].type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].text, 'Hello, there!')
        self.assertEqual(new_nodes[1].url, 'https://www.boot.dev')

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, ' <- this is interesting')
        self.assertEqual(new_nodes[2].url, None)

    def test_split_nodes_image_with_complex_scenario(self):
        nodes = [
            TextNode(
                text="I don't know what to say ",
                type=TextType.TEXT,
            ),
            TextNode(
                text="to you Johnny!",
                type=TextType.BOLD,
            ),
            TextNode(
                text="Oh wow, look at this: ![Image to boot.dev](https://www.boot.dev)",
                type=TextType.TEXT,
            ),
            TextNode(
                text="General Kenobi!",
                type=TextType.TEXT,
            ),
            TextNode(
                text="Hello, there!",
                type=TextType.TEXT,
            ),
            TextNode(
                text="![Free memes](https://www.boot.dev) are the best!",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(len(new_nodes), 8)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "I don't know what to say ")
        self.assertEqual(new_nodes[0].url, None)

        self.assertEqual(new_nodes[1].type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, 'to you Johnny!')
        self.assertEqual(new_nodes[1].url, None)

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, 'Oh wow, look at this: ')
        self.assertEqual(new_nodes[2].url, None)

        self.assertEqual(new_nodes[3].type, TextType.IMAGE)
        self.assertEqual(new_nodes[3].text, 'Image to boot.dev')
        self.assertEqual(new_nodes[3].url, 'https://www.boot.dev')

        self.assertEqual(new_nodes[4].type, TextType.TEXT)
        self.assertEqual(new_nodes[4].text, "General Kenobi!")
        self.assertEqual(new_nodes[4].url, None)

        self.assertEqual(new_nodes[5].type, TextType.TEXT)
        self.assertEqual(new_nodes[5].text, 'Hello, there!')
        self.assertEqual(new_nodes[5].url, None)

        self.assertEqual(new_nodes[6].type, TextType.IMAGE)
        self.assertEqual(new_nodes[6].text, 'Free memes')
        self.assertEqual(new_nodes[6].url, 'https://www.boot.dev')

        self.assertEqual(new_nodes[7].type, TextType.TEXT)
        self.assertEqual(new_nodes[7].text, ' are the best!')
        self.assertEqual(new_nodes[7].url, None)
