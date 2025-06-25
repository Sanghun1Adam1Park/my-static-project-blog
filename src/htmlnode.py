from typing import Self

class HTMLNode():
  def __init__(self, 
               tag: str | None = None, 
               value: str | None = None, 
               children: list[Self] | None = None, 
               props: dict[str, str] | None = None) -> None:
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    if not self.props: return  ""

    str_repr = [f'{k}="{v}"' for k, v in self.props.items()]
    return " " + " ".join(str_repr)

class LeafNode(HTMLNode):
  def __init__(self, 
               tag: str | None,
               value: str,
               props: dict[str, str] | None = None) -> None:
    super().__init__(tag, value, None, props)
  
  def to_html(self):
    if self.value is None: raise ValueError("ERROR: Value is mandatory.")
    if self.tag is None: return self.value
    return f"<{self.tag + super().props_to_html()}>{self.value}</{self.tag}>"
  
  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
  def __init__(self, 
               tag: str, 
               children: list[HTMLNode], 
               props: dict[str, str] | None = None) -> None:
    super().__init__(tag, None, children, props)
  
  def to_html(self):
    if self.tag is None: raise ValueError("Tag cannot be empty")
    if self.children is None or len(self.children) == 0: 
      raise ValueError("Children cannot be empty")

    res = f"<{self.tag + super().props_to_html()}>\n"
    for node in self.children:
      res += node.to_html()
    res += f"\n</{self.tag}>\n"
    return res
  
  def __repr__(self):
    return f"ParentNode({self.tag}, {self.children}, {self.props})"