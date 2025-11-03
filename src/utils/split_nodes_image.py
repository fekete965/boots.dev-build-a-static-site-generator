from src.nodes.textnode import TextNode
from src.nodes.texttype import TextType
from .extract_markdown_images import extract_markdown_images


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []

    for node in old_nodes:
        if node.type != TextType.TEXT:
            result.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if len(images) == 0:
            result.append(node)
            continue

        for img in images:
            (img_text, img_url) = img
            full_img_text = f"![{img_text}]({img_url})"

            partial_text = None

            index_of_img_text = text.find(full_img_text)

            if index_of_img_text == -1:
                raise Exception("Invalid Markdown syntax, image cannot be found")

            partial_text = text[0:index_of_img_text]
            text = text[index_of_img_text + len(full_img_text) :]

            if partial_text is not None and partial_text != "":
                result.append(TextNode(text=partial_text, type=TextType.TEXT))

            result.append(TextNode(text=img_text, type=TextType.IMAGE, url=img_url))

        # Add any remaining text after the last image
        if text is not None and text != "":
            result.append(TextNode(text=text, type=TextType.TEXT))

    return result
