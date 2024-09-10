# O(n) time | O(n)  Space

def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array) - 1)

def constructMinHeightBst(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return

    middleIdx = (startIdx + endIdx) // 2
    newBstNode = BST(array[middleIdx])
    if bst is None:
        bst = newBstNode
    else:
        if array[middleIdx] < bst.value:
            bst.left = newBstNode
            bst = bst.left
        else:
            bst.right = newBstNode
            bst = bst.right
    constructMinHeightBst(array, bst, startIdx, middleIdx - 1)
    constructMinHeightBst(array, bst, middleIdx + 1, endIdx)
    return bst
    
    
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

