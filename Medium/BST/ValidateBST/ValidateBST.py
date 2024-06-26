# Optimal Solution(Recursive)

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_val=float('-inf'), max_val=float('inf')):
    if tree is None:
        return True
    if not (min_val <= tree.value < max_val):
        return False
    return validateBst(tree.left, min_val, tree.value) and validateBst(tree.right, tree.value, max_val)
