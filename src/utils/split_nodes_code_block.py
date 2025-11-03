from src.nodes.textnode import TextNode
from src.nodes.texttype import TextType
import re


def split_nodes_code_block(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Split text nodes on triple backticks (```) for inline code blocks.
    
    Processes text nodes to find triple backtick patterns and converts them
    to CODE_BLOCK text nodes. This function should be called before
    split_nodes_delimiter for single backticks to ensure proper precedence.
    
    Non-TEXT nodes are passed through unchanged. Only TEXT nodes are processed
    for triple backtick patterns.
    
    Args:
        old_nodes: List of TextNode objects to process
        
    Returns:
        List of TextNode objects with triple backtick patterns converted to
        CODE_BLOCK type nodes. Text before and after code blocks remains as
        TEXT type nodes.
        
    Example:
        Input: [TextNode("This is ```code``` here", TextType.TEXT)]
        Output: [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE_BLOCK),
            TextNode(" here", TextType.TEXT)
        ]
    """
    final_nodes = []

    for old in old_nodes:
        if old.type != TextType.TEXT:
            final_nodes.append(old)
            continue

        text = old.text
        # Find all occurrences of triple backticks (including empty code blocks)
        pattern = r'```([^`]*)```'
        matches = list(re.finditer(pattern, text))
        
        if not matches:
            # No triple backticks found, keep the node as is
            final_nodes.append(old)
            continue

        # Split the text based on triple backtick matches
        last_end = 0
        for match in matches:
            # Add text before the match
            if match.start() > last_end:
                before_text = text[last_end:match.start()]
                if before_text:
                    final_nodes.append(TextNode(text=before_text, type=TextType.TEXT))
            
            # Add the code block (content between triple backticks)
            code_content = match.group(1)
            final_nodes.append(TextNode(text=code_content, type=TextType.CODE_BLOCK))
            
            last_end = match.end()
        
        # Add remaining text after the last match
        if last_end < len(text):
            remaining_text = text[last_end:]
            if remaining_text:
                final_nodes.append(TextNode(text=remaining_text, type=TextType.TEXT))

    return final_nodes

