from src.nodes.textnode import TextNode
from src.nodes.texttype import TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    final_nodes = []

    for old in old_nodes:
        if old.type != TextType.TEXT:
            final_nodes.append(old)
            continue

        chunks = old.text.split(delimiter)
        chunks_len = len(chunks)

        if chunks_len == 0:
            continue

        if chunks_len == 1 and chunks[0] == "":
            continue

        if chunks_len == 1 and chunks[0] != "":
            final_nodes.append(TextNode(text=chunks[0], type=TextType.TEXT))
            continue

        if chunks_len % 2 == 0:
            raise Exception("Invalid Markdown syntax")

        for i in range(0, chunks_len):
            text = chunks[i]

            if text == "":
                continue

            if i % 2 == 0:
                final_nodes.append(TextNode(text=text, type=TextType.TEXT))
            else:
                final_nodes.append(TextNode(text=text, type=text_type))

    return final_nodes
