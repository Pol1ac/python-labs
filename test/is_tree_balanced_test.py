import unittest
from src.is_tree_balanced import BinaryTree, is_tree_balanced


class TestIsTreeBalanced(unittest.TestCase):
    def test_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        root = BinaryTree(1)
        self.assertTrue(is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()

