import unittest
from textnode import TextNode, TextType
from functions import text_node_to_html_node

class TestTextNode(unittest.TestCase):
  def test_text(self):
    node = TextNode("This is a text node", TextType.PLAIN)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

  def test_italic(self):
    node = TextNode("This is italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "This is italic text")

  def test_bold(self):
    node = TextNode("This is bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is bold text")

  def test_code(self):
    node = TextNode("This is code", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "This is code")

  def test_link(self):
    node = TextNode("Google", TextType.LINK, "https://www.google.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Google")
    self.assertEqual(html_node.props, {"href": "https://www.google.com"})

  def test_image(self):
    node = TextNode("An image", TextType.IMG, "image.jpg")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "An image")
    self.assertEqual(html_node.props, {"src": "image.jpg"})

  def test_unknown_type(self):
    node = TextNode("Unknown type", "UNKNOWN")
    with self.assertRaises(ValueError) as cm:
      text_node_to_html_node(node)
    self.assertEqual(str(cm.exception), "Unknown text type: UNKNOWN")