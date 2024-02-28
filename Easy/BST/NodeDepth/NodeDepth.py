# Optimal Solution
# Time: O(n)
# Space: O(h) Hight of the Tree

def nodeDepths(root):
    # Write your code here.
    return nodeDepthHelper(root, sums=0)


def nodeDepthHelper(root, sums):

    if root is None:
        return 0

    return sums + nodeDepthHelper(root.left, sums + 1) + nodeDepthHelper(root.right, sums + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
