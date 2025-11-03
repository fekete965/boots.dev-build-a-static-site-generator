import unittest

from .leafnode import LeafNode
from .parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_without_props(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_one_child(self):
        node = ParentNode(
            tag="p",
            children=[LeafNode(tag="span", value="Hello, there!")],
        )
        self.assertEqual(node.to_html(), "<p><span>Hello, there!</span></p>")

    def test_to_html_with_props(self):
        node = ParentNode(
            tag="form",
            children=[LeafNode(tag="h1", value="Hello, there!")],
            props={
                "class": "flex flex-1 justify-between",
                "action": "https://www.boot.dev",
                "method": "POST",
                "id": "login-form",
            },
        )
        self.assertEqual(
            node.to_html(),
            '<form class="flex flex-1 justify-between" action="https://www.boot.dev" method="POST" id="login-form"><h1>Hello, there!</h1></form>',
        )

    def test_to_html_with_complex_nodes(self):
        self.maxDiff = None

        node = ParentNode(
            tag="form",
            children=[
                LeafNode(
                    tag="h1",
                    value="Sign up today!",
                    props={"class": "text-2xl font-bold"},
                ),
                LeafNode(
                    tag="h2",
                    value="Join our community today!",
                    props={"class": "text-lg italic"},
                ),
                ParentNode(
                    tag="div",
                    children=[
                        LeafNode(tag="label", value="First name"),
                        LeafNode(
                            tag="input", value="", props={"type": "text", "name": "first-name"}
                        ),
                    ],
                    props={"class": "flex flex-1 justify-between"},
                ),
                ParentNode(
                    tag="div",
                    children=[
                        LeafNode(tag="label", value="Last name"),
                        LeafNode(
                            tag="input", value="", props={"type": "text", "name": "last-name"}
                        ),
                    ],
                    props={"class": "flex flex-1 justify-between"},
                ),
                ParentNode(
                    tag="div",
                    children=[
                        LeafNode(tag="label", value="Email"),
                        LeafNode(tag="input", value="", props={"type": "email", "name": "email"}),
                    ],
                    props={"class": "flex flex-1 justify-between"},
                ),
                ParentNode(
                    tag="div",
                    children=[
                        LeafNode(tag="label", value="Password"),
                        LeafNode(
                            tag="input", value="", props={"type": "password", "name": "password"}
                        ),
                    ],
                    props={"class": "flex flex-1 justify-between"},
                ),
                ParentNode(
                    tag="div",
                    children=[
                        LeafNode(tag="label", value="Confirm password"),
                        LeafNode(
                            tag="input",
                            value="",
                            props={"type": "password", "name": "confirm-password"},
                        ),
                    ],
                    props={"class": "flex flex-1 justify-between"},
                ),
                ParentNode(
                    tag="div",
                    children=[
                        LeafNode(tag="button", value="Sign up", props={"type": "submit"}),
                    ],
                    props={"class": "flex flex-1 justify-between"},
                ),
                ParentNode(
                    tag="div",
                    children=[
                        ParentNode(
                            tag="p",
                            children=[
                                LeafNode(
                                    tag="",
                                    value="Already have an account? ",
                                ),
                                LeafNode(
                                    tag="a",
                                    value="Login here.",
                                    props={"href": "https://www.boot.dev/login"},
                                ),
                            ],
                        ),
                    ],
                    props={"class": "flex flex-1 justify-between"},
                ),
            ],
            props={
                "class": "flex flex-1 justify-between",
                "action": "https://www.boot.dev",
                "method": "POST",
                "id": "login-form",
            },
        )
        self.assertEqual(
            node.to_html(),
            '<form class="flex flex-1 justify-between" action="https://www.boot.dev" method="POST" id="login-form"><h1 class="text-2xl font-bold">Sign up today!</h1><h2 class="text-lg italic">Join our community today!</h2><div class="flex flex-1 justify-between"><label>First name</label><input type="text" name="first-name" /></div><div class="flex flex-1 justify-between"><label>Last name</label><input type="text" name="last-name" /></div><div class="flex flex-1 justify-between"><label>Email</label><input type="email" name="email" /></div><div class="flex flex-1 justify-between"><label>Password</label><input type="password" name="password" /></div><div class="flex flex-1 justify-between"><label>Confirm password</label><input type="password" name="confirm-password" /></div><div class="flex flex-1 justify-between"><button type="submit">Sign up</button></div><div class="flex flex-1 justify-between"><p>Already have an account? <a href="https://www.boot.dev/login">Login here.</a></p></div></form>',
        )
