import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)
    node3 = TextNode("", TextType.BOLD)
    self.assertNotEqual(node, node3) 
    node4 = TextNode("This is a text node", TextType.PLAIN)
    self.assertNotEqual(node, node4)
    node5 = TextNode("This is a text NODE", TextType.BOLD)
    self.assertNotEqual(node, node5)
    node6 = TextNode("This is a text node", TextType.BOLD, "bood.dev")
    self.assertNotEqual(node, node6)
    node7 = TextNode("This is a text node", TextType.BOLD, "bood.dev")
    self.assertNotEqual(node, node7)

  def test_repr(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD, "boot.dev")
    self.assertEqual(repr(node), 'TextNode(This is a text node, TextType.BOLD, None)')
    self.assertNotEqual(repr(node2), 'TextNode(This is a text node, TextType.BOLD, None)')
    self.assertEqual(repr(node2), 'TextNode(This is a text node, TextType.BOLD, boot.dev)')

if __name__ == "__main__":
  unittest.main()