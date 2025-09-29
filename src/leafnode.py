from htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        node_props = self.props_to_html()
        if node_props != "":
            node_props = " " + node_props

        return f"<{self.tag}{node_props}>{self.value}</{self.tag}>"
