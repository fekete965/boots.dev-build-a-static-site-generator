import re


# Markdown link: [title](https://www.example.com)
def extract_markdown_links(text: str) -> list[(str, str)]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
