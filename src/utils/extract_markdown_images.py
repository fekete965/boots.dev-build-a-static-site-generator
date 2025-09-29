import re


# Markdown image: ![alt text](image.jpg)
def extract_markdown_images(text: str) -> list[(str, str)]:
    return re.findall(r'\!\[(.*?)\]\((.*?)\)', text)
