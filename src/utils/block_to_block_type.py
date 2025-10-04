from src.nodes.blocktype import BlockType
import re


def block_to_block_type(block: str) -> BlockType:
    # Checking for heading block
    if re.match(r'#{1,6}\s.+', block):
        return BlockType.HEADING

    # Checking for code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Checking for unordered list
    if block.startswith("*") or block.startswith("-") or block.startswith("+"):
        return BlockType.UNORDERED_LIST

    # Checking for ordered list
    if re.match(r'^[0-9]+\.', block):
        return BlockType.ORDERED_LIST

    # Checking for quote
    if block.startswith(">"):
        return BlockType.QUOTE

    # Otherwise, it's a paragraph
    return BlockType.PARAGRAPH
