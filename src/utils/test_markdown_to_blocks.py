import unittest

from .markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_single_block(self):
        markdown = "Hello, there!"
        blocks = markdown_to_blocks(markdown)

        self.assertEqual(len(blocks), 1)

        self.assertEqual(blocks, ["Hello, there!"])

    def test_markdown_to_blocks_strip_whitespace(self):
        markdown = "    Hello, there!     \n\n Ahoy matey    "
        blocks = markdown_to_blocks(markdown)

        self.assertEqual(len(blocks), 2)

        self.assertEqual(blocks, ["Hello, there!", "Ahoy matey"])

    def test_markdown_to_blocks_multiple_block(self):
        self.maxDiff = None

        # We need this weird spacing to test the whitespace stripping.
        # If we indent it the tabs will be included in the blocks.
        # It would make our test fail.
        markdown = """
# **OBI-WAN**: Hello, there!

# _GENERAL GRIEVOUS_: General Kenobi, you are a bold one. I find your behavior bewildering . . . Surely you realize you're doomed, (to droids) Kill him!

## About a HUNDRED BATTLE DROIDS surround OBI-WAN, GENERAL GRIEVOUS, and his BODYGUARDS.
OBI-WAN looks around, then walks right up to GENERAL GRIEVOUS.
They stare at each other for a moment.

# _GENERAL GRIEVOUS_: Enough of this.
         """
        blocks = markdown_to_blocks(markdown)

        self.assertEqual(len(blocks), 4)

        self.assertEqual(
            blocks,
            [
                "# **OBI-WAN**: Hello, there!",
                "# _GENERAL GRIEVOUS_: General Kenobi, you are a bold one. I find your behavior bewildering . . . Surely you realize you're doomed, (to droids) Kill him!",
                "## About a HUNDRED BATTLE DROIDS surround OBI-WAN, GENERAL GRIEVOUS, and his BODYGUARDS.\nOBI-WAN looks around, then walks right up to GENERAL GRIEVOUS.\nThey stare at each other for a moment.",
                "# _GENERAL GRIEVOUS_: Enough of this.",
            ],
        )
