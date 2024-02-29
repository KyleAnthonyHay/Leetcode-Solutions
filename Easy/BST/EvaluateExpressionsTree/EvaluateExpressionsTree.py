# Optimal Solution
# Time: O(n)
# Space: O(h) height of Tree

# Solution 1
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value

    left = evaluateExpressionTree(tree.left)
    right = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return left + right
    if tree.value == -2:
        return left - right
    if tree.value == -3:
        return int(left / right)

    return left * right

# Solution 2


def evaluateExpressionTree(tree):

    return evaluateExpressionTreeHelper(tree,  result=0)


def evaluateExpressionTreeHelper(tree,  result):
    if tree.value >= 0:
        return tree.value

    left = evaluateExpressionTree(tree.left)
    right = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return result + (left + right)
    if tree.value == -2:
        return result + (left - right)
    if tree.value == -3:
        return result + int(left / right)

    return result + (left * right)
