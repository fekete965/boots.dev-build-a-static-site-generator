import unittest

from .htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(
            tag='a',
            value=None,
            children=None,
            props={
                "class": "flex flex-1 justify-between",
                "id": "main",
                "href": "https://www.boot.dev",
            },
        )

        self.assertEqual(
            node.props_to_html(),
            'class="flex flex-1 justify-between" id="main" href="https://www.boot.dev"',
        )

    def test_props_to_html_with_no_props(self):
        node = HtmlNode(
            tag='div',
            value=None,
            children=None,
            props=None,
        )

        self.assertEqual(node.props_to_html(), "")

    def test_repr_without_children(self):
        node = HtmlNode(
            tag='div',
            value="Hello, there!",
            children=None,
            props={"id": "wrapper"},
        )

        self.assertEqual(
            repr(node), "HtmlNode(div, Hello, there!, None, {'id': 'wrapper'})")

    def test_repr_with_children(self):
        node = HtmlNode(
            tag='div',
            value="Hello, there!",
            children=[
                HtmlNode(tag='p', value="This is a paragraph", children=None, props=None)],
            props={"id": "wrapper"},
        )

        self.assertEqual(repr(
            node), "HtmlNode(div, Hello, there!, [HtmlNode(p, This is a paragraph, None, None)], {'id': 'wrapper'})")
