from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag: str,  children: list["HtmlNode"], props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None")

        if self.children is None:
            raise ValueError("Children cannot be None")

        node_props = self.props_to_html()
        if node_props != "":
            node_props = " " + node_props

        children_html = "".join(
            map(lambda child: child.to_html(), self.children)
        )

        return f"<{self.tag}{node_props}>{children_html}</{self.tag}>"
