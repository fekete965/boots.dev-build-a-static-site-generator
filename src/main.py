from textnode import TextNode
from texttype import TextType


def main():
    text_node = TextNode(
        text="This is some anchor text",
        type=TextType.LINK,
        url="https://www.boot.dev",
    )
    print(text_node)


if __name__ == "__main__":
    main()
