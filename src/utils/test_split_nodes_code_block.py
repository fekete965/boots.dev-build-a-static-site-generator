import unittest

from src.nodes.textnode import TextNode
from src.nodes.texttype import TextType
from .split_nodes_code_block import split_nodes_code_block


class TestSplitNodesCodeBlock(unittest.TestCase):
    def test_split_nodes_code_block_no_code_blocks_single_node(self):
        nodes = [TextNode(text="Hello, there!", type=TextType.TEXT)]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 1)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Hello, there!')

    def test_split_nodes_code_block_no_code_blocks_multiple_nodes(self):
        nodes = [
            TextNode(text="Hello, there!", type=TextType.TEXT),
            TextNode(text="Ahoy, matey!", type=TextType.TEXT),
            TextNode(text="Howdy, partner!", type=TextType.TEXT),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 3)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Hello, there!')

        self.assertEqual(new_nodes[1].type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, 'Ahoy, matey!')

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, 'Howdy, partner!')

    def test_split_nodes_code_block_with_single_code_block_node(self):
        nodes = [
            TextNode(
                text="```code example```",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 1)

        self.assertEqual(new_nodes[0].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[0].text, 'code example')

    def test_split_nodes_code_block_with_multiple_code_block_nodes(self):
        nodes = [
            TextNode(
                text="```first code```",
                type=TextType.TEXT,
            ),
            TextNode(
                text="```second code```",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 2)

        self.assertEqual(new_nodes[0].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[0].text, 'first code')

        self.assertEqual(new_nodes[1].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[1].text, 'second code')

    def test_split_nodes_code_block_with_single_node_that_contains_a_single_code_block_at_the_end_of_the_text(self):
        nodes = [
            TextNode(
                text="Oh wow, look at this: ```code example```",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 2)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Oh wow, look at this: ')

        self.assertEqual(new_nodes[1].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[1].text, 'code example')

    def test_split_nodes_code_block_with_single_node_that_contains_a_single_code_block_at_the_beginning_of_the_text(self):
        nodes = [
            TextNode(
                text="```code example``` <- this is interesting",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 2)

        self.assertEqual(new_nodes[0].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[0].text, 'code example')

        self.assertEqual(new_nodes[1].type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, ' <- this is interesting')

    def test_split_nodes_code_block_with_single_node_that_contains_a_single_code_block_in_the_middle_of_the_text(self):
        nodes = [
            TextNode(
                text="Oh wow, look at this: ```code example``` <- this is interesting",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 3)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Oh wow, look at this: ')

        self.assertEqual(new_nodes[1].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[1].text, 'code example')

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, ' <- this is interesting')

    def test_split_nodes_code_block_with_complex_scenario(self):
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
                text="Oh wow, look at this: ```code example```",
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
                text="```more code``` are the best!",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 8)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "I don't know what to say ")

        self.assertEqual(new_nodes[1].type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, 'to you Johnny!')

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, 'Oh wow, look at this: ')

        self.assertEqual(new_nodes[3].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[3].text, 'code example')

        self.assertEqual(new_nodes[4].type, TextType.TEXT)
        self.assertEqual(new_nodes[4].text, "General Kenobi!")

        self.assertEqual(new_nodes[5].type, TextType.TEXT)
        self.assertEqual(new_nodes[5].text, 'Hello, there!')

        self.assertEqual(new_nodes[6].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[6].text, 'more code')

        self.assertEqual(new_nodes[7].type, TextType.TEXT)
        self.assertEqual(new_nodes[7].text, ' are the best!')

    def test_split_nodes_code_block_preserves_non_text_nodes(self):
        nodes = [
            TextNode(text="Some text", type=TextType.TEXT),
            TextNode(text="bold text", type=TextType.BOLD),
            TextNode(text="```code```", type=TextType.TEXT),
            TextNode(text="italic text", type=TextType.ITALIC),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 4)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Some text')

        self.assertEqual(new_nodes[1].type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, 'bold text')

        self.assertEqual(new_nodes[2].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[2].text, 'code')

        self.assertEqual(new_nodes[3].type, TextType.ITALIC)
        self.assertEqual(new_nodes[3].text, 'italic text')

    def test_split_nodes_code_block_with_empty_code_block(self):
        nodes = [
            TextNode(
                text="``````",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 1)

        self.assertEqual(new_nodes[0].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[0].text, '')

    def test_split_nodes_code_block_with_code_block_containing_spaces(self):
        nodes = [
            TextNode(
                text="Here is ```code with spaces``` in text",
                type=TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_code_block(nodes)

        self.assertEqual(len(new_nodes), 3)

        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, 'Here is ')

        self.assertEqual(new_nodes[1].type, TextType.CODE_BLOCK)
        self.assertEqual(new_nodes[1].text, 'code with spaces')

        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, ' in text')

