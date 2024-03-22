# Optimal Solution
# Time: O(n)
# Space: O(n)

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    branchSumsHelper(root, 0, sums)
    return sums


def branchSumsHelper(node, branchSum, sums):
    if node is None:
        return

    branchSum += node.value
    if node.left is None and node.right is None:  # Base case
        sums.append(branchSum)
        return

    branchSumsHelper(node.left, branchSum, sums)
    branchSumsHelper(node.right, branchSum, sums)
