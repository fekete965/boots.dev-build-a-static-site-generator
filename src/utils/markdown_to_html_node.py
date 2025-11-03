import re
from src.nodes.blocktype import BlockType
from src.nodes.htmlnode import HtmlNode
from src.nodes.leafnode import LeafNode
from src.nodes.parentnode import ParentNode
from .text_node_to_html_node import text_node_to_html_node
from .text_to_textnodes import text_to_text_nodes
from .markdown_to_blocks import markdown_to_blocks
from .block_to_block_type import block_to_block_type


def markdown_to_html_node(markdown: str) -> HtmlNode:
    """
    Convert markdown text to an HTML node tree.

    Parses markdown text by splitting it into blocks, identifying each block's
    type (heading, code, list, quote, paragraph), and converting each block
    to appropriate HTML nodes. All blocks are wrapped in a root <div> element.

    Args:
        markdown: Multi-line markdown text string

    Returns:
        ParentNode with tag "div" containing all converted HTML nodes

    Example:
        Input: "# Heading\n\nSome paragraph text"
        Output: ParentNode(tag="div", children=[
            ParentNode(tag="h1", children=[...]),
            ParentNode(tag="p", children=[...])
        ])
    """
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.HEADING:
                node = heading_to_html_node(block)
                html_nodes.append(node)
            case BlockType.CODE:
                node = code_to_html_node(block)
                html_nodes.append(node)
            case BlockType.UNORDERED_LIST:
                node = unordered_list_to_html_node(block)
                html_nodes.append(node)
            case BlockType.PARAGRAPH:
                node = paragraph_to_html_node(block)

                # If node is a div wrapping only an image (or image + trailing text), unwrap it
                if node.tag == "div":
                    html_nodes.extend(node.children)
                else:
                    html_nodes.append(node)
            case BlockType.QUOTE:
                node = quote_to_html_node(block)
                html_nodes.append(node)
            case BlockType.ORDERED_LIST:
                node = ordered_list_to_html_node(block)
                html_nodes.append(node)

    parent_node = ParentNode(tag="div", children=html_nodes)
    return parent_node


def text_to_children(text: str) -> list[HtmlNode]:
    """
    Convert text string to a list of HTML node children.

    Processes text to extract markdown elements and converts each TextNode
    to its HTML representation.

    Args:
        text: Text string potentially containing markdown syntax

    Returns:
        List of HtmlNode objects representing the parsed text
    """
    text_nodes = text_to_text_nodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def heading_to_html_node(heading: str) -> HtmlNode:
    """
    Convert a markdown heading to an HTML heading node.

    Parses heading levels 1-6 based on the number of # symbols at the start.
    The heading text may contain inline markdown which is processed.

    Args:
        heading: Markdown heading string (e.g., "# Heading", "## Subheading")

    Returns:
        ParentNode with tag h1-h6 containing the heading text as children

    Raises:
        ValueError: If the heading format is invalid
    """
    for i in range(6, 0, -1):
        heading_symbols = "#" * i

        if heading.startswith(heading_symbols):
            heading_symbol_len = len(heading_symbols)
            heading = heading[heading_symbol_len:].strip()

            children = text_to_children(heading)

            return ParentNode(tag=f"h{i}", children=children)

    raise ValueError(f"Invalid heading: {heading}")


def code_to_html_node(code: str) -> HtmlNode:
    """
    Convert a markdown code block to an HTML code node.

    Handles both triple backticks (```) for code blocks and single backticks (`)
    for inline code. Triple backticks are wrapped in <pre><code> tags, while
    single backticks are wrapped only in <code> tags.

    Args:
        code: Markdown code string (either ```code``` or `code`)

    Returns:
        ParentNode with tag "pre" and child LeafNode with tag "code" for triple
        backticks, or LeafNode with tag "code" for single backticks

    Raises:
        ValueError: If the code format is invalid
    """
    code = code.strip()

    if code.startswith("```") and code.endswith("```"):
        code = code[3:-3]

        children = [LeafNode(tag="code", value=code)]
        return ParentNode(tag="pre", children=children)

    if code.startswith("`") and code.endswith("`"):
        code = code[1:-1]

        return LeafNode(tag="code", value=code)

    raise ValueError(f"Invalid code: {code}")


def unordered_list_to_html_node(unordered_list: str) -> HtmlNode:
    """
    Convert a markdown unordered list to an HTML unordered list node.

    Parses list items starting with *, -, or + prefixes. Each list item
    may contain inline markdown which is processed.

    Args:
        unordered_list: Multi-line markdown unordered list string

    Returns:
        ParentNode with tag "ul" containing list item nodes as children
    """
    list_items = unordered_list.split("\n")

    html_nodes = []

    for item in list_items:
        item = item.strip()
        item_text = item

        if item.startswith("* ") or item.startswith("- ") or item.startswith("+ "):
            item_text = item[2:].strip()
        elif item.startswith("*") or item.startswith("-") or item.startswith("+"):
            item_text = item[1:].strip()

        children = text_to_children(item_text)
        list_item_node = ParentNode(tag="li", children=children)
        html_nodes.append(list_item_node)

    return ParentNode(tag="ul", children=html_nodes)


def paragraph_to_html_node(paragraph: str) -> HtmlNode:
    """
    Convert markdown paragraph text to an HTML paragraph node.

    Normalizes whitespace and processes inline markdown. If the paragraph
    starts with an image or link, it wraps children in a <div> instead of <p>.

    Args:
        paragraph: Paragraph text string potentially containing markdown syntax

    Returns:
        ParentNode with tag "p" for normal paragraphs or "div" for paragraphs
        starting with images or links
    """
    cleaned_text = paragraph.replace("\n", " ").strip()
    children = text_to_children(cleaned_text)

    if children and children[0].tag in ("img", "a"):
        return ParentNode(tag="div", children=children)

    return ParentNode(tag="p", children=children)


def quote_to_html_node(quote: str) -> HtmlNode:
    """
    Convert a markdown blockquote to an HTML blockquote node.

    Parses lines starting with > and removes the quote prefix. Processes
    inline markdown within the quote text.

    Args:
        quote: Multi-line markdown blockquote string

    Returns:
        ParentNode with tag "blockquote" containing the quote text as children
    """
    lines = quote.split("\n")

    cleaned_lines = []
    for line in lines:
        if line.startswith("> "):
            cleaned_lines.append(line[2:].strip())
        elif line.startswith(">"):
            cleaned_lines.append(line[1:].strip())
        else:
            cleaned_lines.append(line.strip())

    cleaned_text = " ".join(cleaned_lines).strip()
    children = text_to_children(cleaned_text)

    return ParentNode(tag="blockquote", children=children)


def ordered_list_to_html_node(ordered_list: str) -> HtmlNode:
    """
    Convert a markdown ordered list to an HTML ordered list node.

    Parses list items with numbered prefixes (1., 2., etc.) and removes
    the numbering. Each list item may contain inline markdown which is processed.

    Args:
        ordered_list: Multi-line markdown ordered list string

    Returns:
        ParentNode with tag "ol" containing list item nodes as children
    """
    list_items = ordered_list.split("\n")

    html_nodes = []

    for item in list_items:
        item_text = re.sub(r"^\d+\.\s*", "", item.strip()).strip()
        children = text_to_children(item_text)
        list_item_node = ParentNode(tag="li", children=children)
        html_nodes.append(list_item_node)

    return ParentNode(tag="ol", children=html_nodes)
