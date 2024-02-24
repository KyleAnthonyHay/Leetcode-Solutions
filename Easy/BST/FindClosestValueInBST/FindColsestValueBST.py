# First Solution(Recursive)
# Time: O(logn) Number of nodes(O(n) worst case)
# Space: O(logn) Frames on the call stack(for the recursive calls)

def findClosestValueInBst(tree, target):
    # Write your code here.

    return findClosestValueInBstHelper(tree, target, float("inf"))


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:  # Base Case
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    elif target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Optimal Solution(Iterative)

def findClosestValueInBstHelper_Iterative(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value

        if target > currentNode.value:
            currentNode = currentNode.right
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            return closest
    return closest
