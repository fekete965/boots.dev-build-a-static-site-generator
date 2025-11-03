import inspect
import unittest

from .markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def text_heading1(self):
        expected_html = "<div><h1>Hello, there heading 1!</h1></div>"
        
        markdown_text = inspect.cleandoc("""# Hello, there heading 1!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        markdown_text = inspect.cleandoc("""#Hello, there heading 1!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        
    def text_heading2(self):
        expected_html = "<div><h2>Hello, there heading 2!</h2></div>"
        
        markdown_text = inspect.cleandoc("""## Hello, there heading 2!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        markdown_text = inspect.cleandoc("""##Hello, there heading 2!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        
    def text_heading3(self):
        expected_html = "<div><h3>Hello, there heading 3!</h3></div>"
        
        markdown_text = inspect.cleandoc("""### Hello, there heading 3!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

        markdown_text = inspect.cleandoc("""###Hello, there heading 3!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        
    def text_heading4(self):
        expected_html = "<div><h4>Hello, there heading 4!</h4></div>"
        
        markdown_text = inspect.cleandoc("""#### Hello, there heading 4!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        markdown_text = inspect.cleandoc("""####Hello, there heading 4!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        
    def text_heading5(self):
        expected_html = "<div><h5>Hello, there heading 5!</h5></div>"
        markdown_text = inspect.cleandoc("""##### Hello, there heading 5!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

        markdown_text = inspect.cleandoc("""#####Hello, there heading 5!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
   
   
    def text_heading6(self):
        expected_html = "<div><h6>Hello, there heading 6!</h6></div>"
        
        markdown_text = inspect.cleandoc("""###### Hello, there heading 6!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

        markdown_text = inspect.cleandoc("""######Hello, there heading 6!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        
    def text_heading_above_6(self):
        expected_html = "<div><h6>Hello, there heading 7!</h6></div>"
        
        markdown_text = inspect.cleandoc("""####### Hello, there heading 7!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

        
        markdown_text = inspect.cleandoc("""#######Hello, there heading 7!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        
    def text_paragraph(self):
        expected_html = "<div><p>This is a paragraph! What a surprise!</p></div>"
        markdown_text = inspect.cleandoc("""This is a paragraph! What a surprise!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
    
    
    def text_bold(self):
        expected_html = "<div><b>This is a bold text</b></div>"
        markdown_text = inspect.cleandoc("""This is a *bold* text""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
    
    
    def text_italic(self):
        expected_html = "<div><p>This is an __italic__ text</p></div>"
        markdown_text = inspect.cleandoc("""This is an <i>italic</i> text""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        
    def test_ordered_list(self):
        expected_html = "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"
        
        markdown_text = inspect.cleandoc("""
        1. First item
        2. Second item
        3. Third item""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
   
   
    def test_unordered_list(self):
        expected_html = "<div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>"
        
        markdown_text = inspect.cleandoc("""
        * First item
        * Second item
        * Third item""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
       
        markdown_text = inspect.cleandoc("""
        *First item
        *Second item
        *Third item""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
   
        markdown_text = inspect.cleandoc("""
        + First item
        + Second item
        + Third item""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        markdown_text = inspect.cleandoc("""
        +First item
        +Second item
        +Third item""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        markdown_text = inspect.cleandoc("""
        - First item
        - Second item
        - Third item""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
        
        markdown_text = inspect.cleandoc("""
        -First item
        -Second item
        -Third item""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
   
    def test_blockquote(self):
        expected_html = "<div><blockquote>blockquote example.</blockquote></div>"
        
        markdown_text = inspect.cleandoc("""> blockquote example.""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
   
   
    def test_inline_codeblock(self):
        expected_html = "<div><code>code example, meh?</code></div>"
        
        markdown_text = inspect.cleandoc("""`code example, meh?`""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

    def test_codeblock(self):
        expected_html = "<div><pre><code>code example, meh?</code></pre></div>"
        
        markdown_text = inspect.cleandoc("""```code example, meh?```""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
    
    def test_link(self):
        expected_html = "<div><a href=\"https://example.com\">this amazing link</a></div>"
        markdown_text = inspect.cleandoc("""[this amazing link](https://example.com)""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)


    def test_image(self):
        expected_html = "<div><img src=\"https://example.com/img.png\" alt=\"cool image\" />!</div>"
        markdown_text = inspect.cleandoc("""![cool image](https://example.com/img.png)!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
    
    
    def test_paragraph_with_inline_markdown(self):
        expected_html = "<div><p>This is <b>bold</b> and <i>italic</i> with <pre><code>code</code></pre> here</p></div>"
        markdown_text = inspect.cleandoc("""This is *bold* and _italic_ with ```code``` here""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)


    def test_heading_with_inline_markdown(self):
        expected_html = "<div><h1>Hello <b>bold</b> world</h1></div>"
        markdown_text = inspect.cleandoc("""# Hello *bold* world""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)


    def test_list_with_inline_markdown(self):
        expected_html = "<div><ul><li>Item with <b>bold</b></li><li>Item with <i>italic</i></li></ul></div>"
        markdown_text = inspect.cleandoc("""
        * Item with *bold*
        * Item with _italic_
        """)
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)


    def test_paragraph_with_link(self):
        expected_html = "<div><p>Check out <a href=\"https://example.com\">this link</a> for more info</p></div>"
        markdown_text = inspect.cleandoc("""Check out [this link](https://example.com) for more info""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)


    def test_paragraph_with_image(self):
        expected_html = "<div><p>Here's an image <img src=\"https://example.com/img.png\" alt=\"cool image\" />!</p></div>"
        markdown_text = inspect.cleandoc("""Here's an image ![cool image](https://example.com/img.png)!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)


    def test_complex_markdown_document(self):
        expected_html = "<div><h1>My Blog Post</h1><p>Welcome to my <b>awesome</b> blog!</p><ul><li>First point</li><li>Second point with <i>emphasis</i></li></ul><blockquote>Great quote here</blockquote><p>More content with a <a href=\"https://example.com\">link</a>.</p></div>"
        
        markdown_text = inspect.cleandoc("""
        # My Blog Post
        
        Welcome to my *awesome* blog!
        
        * First point
        * Second point with _emphasis_
        
        > Great quote here
        
        More content with a [link](https://example.com).
        """)
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

    
    def test_empty_string(self):
        expected_html = "<div></div>"
        markdown_text = inspect.cleandoc("")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

    
    def test_only_whitespace(self):
        expected_html = "<div></div>"
        markdown_text = inspect.cleandoc("   \n\n   \n\n   ")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

    
    def test_paragraph_with_multiple_newlines(self):
        expected_html = "<div><p>This is a paragraph with newlines that become spaces</p></div>"
        markdown_text = inspect.cleandoc("""This is a paragraph
        with newlines
        that become spaces""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)

    
    def test_ordered_list_with_inline_markdown(self):
        expected_html = "<div><ol><li>Buy <b>milk</b></li><li>Buy <i>eggs</i></li><li>Buy <pre><code>code</code></pre></li></ol></div>"
        markdown_text = inspect.cleandoc("""
        1. Buy *milk*
        2. Buy _eggs_
        3. Buy ```code```
        """)
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)


    def test_mixed_inline_markdown(self):
        expected_html = "<div><p>This has <b>bold</b>, <i>italic</i>, <pre><code>code</code></pre>, <a href=\"https://example.com\">link</a>, and <img src=\"https://example.com/img.png\" alt=\"image\" />!</p></div>"
        markdown_text = inspect.cleandoc("""This has *bold*, _italic_, ```code```, [link](https://example.com), and ![image](https://example.com/img.png)!""")
        node = markdown_to_html_node(markdown_text)
        self.assertEqual(node.to_html(), expected_html)
