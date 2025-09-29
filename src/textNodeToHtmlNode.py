from htmlnode import HtmlNode
from leafnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node: TextNode) -> HtmlNode:
    match text_node.type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value=text_node.text, props={"src": text_node.url})
