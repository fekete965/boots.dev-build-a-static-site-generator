from src.nodes.textnode import TextNode
from src.nodes.texttype import TextType
from .split_nodes_delimiter import split_nodes_delimiter
from .split_nodes_image import split_nodes_image
from .split_nodes_link import split_nodes_link


def text_to_text_nodes(text: str) -> list[TextNode]:
    old_nodes = [TextNode(text=text, type=TextType.TEXT)]

    old_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
    old_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
    old_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
    old_nodes = split_nodes_image(old_nodes)
    old_nodes = split_nodes_link(old_nodes)

    return old_nodes
