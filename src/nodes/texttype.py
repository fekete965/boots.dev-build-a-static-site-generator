from enum import Enum


class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    CODE_BLOCK = 'code_block'
    LINK = 'link'
    IMAGE = 'image'
