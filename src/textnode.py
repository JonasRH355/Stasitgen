from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic" 
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    pass

class TextNode():
    def __init__(self,text,texttype,url=None):
        self.text = text
        self.text_type = texttype
        self.url = url
    
    def __eq__(self, other: TextType):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
