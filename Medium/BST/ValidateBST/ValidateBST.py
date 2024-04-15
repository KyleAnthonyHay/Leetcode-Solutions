# Optimal Solution(Recursive)

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    if tree == None:
        return True

    if tree.left is not None and tree.left.value >= tree.value:
        return False
    if tree.right is not None and tree.right.value < tree.value:
        return False

    return validateBst(tree.left) and validateBst(tree.right)
