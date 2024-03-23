import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("h1", "Spaghet")
        node2 = LeafNode("b", "Spaghet")
        node3 = LeafNode("a", "Streamer", {"href": "notarealaccount.com"})
        node5 = LeafNode("h1", "Spaghet")
        self.assertEqual(node, node5)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node5)
        self.assertNotEqual(node, node3)

if __name__ == "__main__":
    unittest.main()