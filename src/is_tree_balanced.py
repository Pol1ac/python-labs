class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_tree_balanced(node):
    result, _=_is_tree_balanced(node)
    return result


def _is_tree_balanced(node):
    if node is None:
        return True, 0

    left_balance, left_height = _is_tree_balanced(node.left)
    right_balance, right_height = _is_tree_balanced(node.right)

    if abs(left_height - right_height) <= 1 and left_balance and right_balance:
        return True, max(left_height, right_height) + 1

    return False, max(left_height, right_height) + 1
