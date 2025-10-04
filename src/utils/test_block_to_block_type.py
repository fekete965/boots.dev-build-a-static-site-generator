import unittest
from src.nodes.blocktype import BlockType
from .block_to_block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading1(self):
        block = "# Hello, there heading 1!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

        block = "## Hello, there heading 2!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

        block = "### Hello, there heading 3!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        block = "#### Hello, there heading 4!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        block = "##### Hello, there heading 5!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

        block = "###### Hello, there heading 6!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```python\nprint('Hello, there code!')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_unordered_list(self):
        block = "* Hello, there unordered list!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. Buy milk"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

        block = "2. Buy bread"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

        block = "3. Buy eggs"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_quote(self):
        block = "> Hello, there quote!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_paragraph(self):
        block = "Hello, there paragraph!"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
