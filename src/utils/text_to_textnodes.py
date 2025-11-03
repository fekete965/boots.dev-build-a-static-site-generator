from src.nodes.textnode import TextNode
from src.nodes.texttype import TextType
from .split_nodes_delimiter import split_nodes_delimiter
from .split_nodes_code_block import split_nodes_code_block
from .split_nodes_image import split_nodes_image
from .split_nodes_link import split_nodes_link


def text_to_text_nodes(text: str) -> list[TextNode]:
    """
    Convert a plain text string into a list of TextNode objects with appropriate types.
    
    Processes the text to identify and extract various markdown elements including:
    - Triple backtick code blocks (```code```)
    - Bold text (*text*)
    - Italic text (_text_)
    - Single backtick inline code (`code`)
    - Images (![alt](url))
    - Links ([text](url))
    
    The processing order is important: code blocks are processed first to avoid
    conflicts with single backticks, then bold/italic, then single backticks,
    and finally images and links.
    
    Args:
        text: Plain text string potentially containing markdown syntax
        
    Returns:
        List of TextNode objects with appropriate types based on the markdown
        syntax found in the input text
        
    Example:
        Input: "This is *bold* and ```code```"
        Output: [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE_BLOCK)
        ]
    """
    old_nodes = [TextNode(text=text, type=TextType.TEXT)]

    old_nodes = split_nodes_code_block(old_nodes)
    old_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
    old_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
    old_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
    old_nodes = split_nodes_image(old_nodes)
    old_nodes = split_nodes_link(old_nodes)

    return old_nodes
