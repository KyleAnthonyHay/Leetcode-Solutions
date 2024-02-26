# Optimal Solution
# Time: O(logn) Number of nodes(O(n) worst case)
# Space: O(logn) Frames on the call stack(for the recursive calls)

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
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
