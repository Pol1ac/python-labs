import lab_3
import unittest

class TestIsTreeBalanced(unittest.TestCase):
    def test_balanced_tree(self):
        root = lab_3.BinaryTree(1)
        root.left = lab_3.BinaryTree(2)
        root.right = lab_3.BinaryTree(3)
        root.left.left = lab_3.BinaryTree(4)
        root.left.right = lab_3.BinaryTree(5)
        self.assertTrue(lab_3.is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = lab_3.BinaryTree(1)
        root.left = lab_3.BinaryTree(2)
        root.left.left = lab_3.BinaryTree(3)
        self.assertFalse(lab_3.is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(lab_3.is_tree_balanced(None))

    def test_single_node_tree(self):
        root = lab_3.BinaryTree(1)
        self.assertTrue(lab_3.is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()

