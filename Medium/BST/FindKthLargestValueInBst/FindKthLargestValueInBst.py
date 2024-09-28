# O(h + k) time | O(h)  Space

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue
        
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    
    return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
    if node == None or treeInfo.numberOfNodesVisited >= k:
        return
    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)


    