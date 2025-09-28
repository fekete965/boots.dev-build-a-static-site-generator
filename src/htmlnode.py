from functools import reduce


class HtmlNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list["HtmlNode"] = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""

        return " ".join(map(lambda item: f"{item[0]}=\"{item[1]}\"", self.props.items()))

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
