from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
  text_type: TextType = text_node.text_type
  match text_type:
    case TextType.PLAIN:
      return LeafNode(None, text_node.text)
    case TextType.ITALIC:
      return LeafNode("i", text_node.text)
    case TextType.BOLD:
      return LeafNode("b", text_node.text)
    case TextType.CODE:
      return LeafNode("code", text_node.text)
    case TextType.LINK:
      return LeafNode("a", text_node.text, {"href": text_node.url})
    case TextType.IMG:
      return LeafNode("img", text_node.text, {"src": text_node.url})
    case _:
      raise ValueError(f"Unknown text type: {text_type}")