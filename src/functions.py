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

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.PLAIN:
      new_nodes.append(old_node)
      continue
    split = old_node.text.split(delimiter)
    if len(split)%2 == 0:
      raise ValueError("ERROR: Unclosed delimiter.")
    new_node = []
    for i, s in enumerate(split):
      if s == "": continue
      if i%2 == 0:
        new_node.append(TextNode(s, TextType.PLAIN))
      else:
        new_node.append(TextNode(s, text_type))
    new_nodes.extend(new_node)
  return new_nodes