from src.nodes.texttype import TextType


class TextNode():
    def __init__(self, text: str, type: TextType, url: str = None):
        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.type == other.type and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
