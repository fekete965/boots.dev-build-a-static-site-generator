from src.nodes.textnode import TextNode, TextType
from .extract_markdown_links import extract_markdown_links


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []

    for node in old_nodes:
        if node.type != TextType.TEXT:
            result.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if (len(links) == 0):
            result.append(node)
            continue

        for link in links:
            (link_text, link_url) = link
            full_link_text = f"[{link_text}]({link_url})"

            partial_text = None

            index_of_link_text = text.find(full_link_text)

            if index_of_link_text == -1:
                raise Exception(
                    "Invalid Markdown syntax, link cannot be found"
                )

            partial_text = text[0:index_of_link_text]
            text = text[index_of_link_text + len(full_link_text):]

            if partial_text is not None and partial_text != "":
                result.append(TextNode(text=partial_text, type=TextType.TEXT))

            result.append(
                TextNode(text=link_text, type=TextType.LINK, url=link_url)
            )

        # Add any remaining text after the last link
        if text is not None and text != "":
            result.append(TextNode(text=text, type=TextType.TEXT))

    return result
