# Time: O(n) | Space: O(h)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx


def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBSTFromRange(float('-inf'),float('inf'), preOrderTraversalValues, treeInfo)

def reconstructBSTFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None
        
    rootvalue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootvalue < lowerBound or rootvalue >= upperBound:
        return None

    currentSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBSTFromRange(lowerBound, rootvalue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBSTFromRange(rootvalue, upperBound, preOrderTraversalValues, currentSubtreeInfo) 

    return BST(rootvalue, leftSubtree, rightSubtree)