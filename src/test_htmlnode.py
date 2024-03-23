import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "Spaghet")
        node2 = HTMLNode("h1", "Spaghet")
        node3 = HTMLNode("h1", "Spaghet", [node, node2])
        node4 = HTMLNode("h1", "Spaghet", props={"href": "notarealaccount.com"})
        node5 = HTMLNode("h1", "Spaghet", [node, node2])
        self.assertEqual(node, node2)
        self.assertEqual(node3, node5)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)

if __name__ == "__main__":
    unittest.main()