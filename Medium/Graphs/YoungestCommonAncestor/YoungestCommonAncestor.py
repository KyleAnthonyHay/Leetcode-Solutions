# Time O(D) | Space O(1)

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = 0
    depthTwo = 0
    nodeOne = descendantOne
    nodeTwo = descendantTwo
    
    while nodeOne.ancestor is not None:
        depthOne += 1
        nodeOne = nodeOne.ancestor
    while nodeTwo.ancestor is not None:
        depthTwo += 1
        nodeTwo = nodeTwo.ancestor
    
    if depthOne < depthTwo:
        difference = depthTwo - depthOne
        for i in range(difference):
            descendantTwo = descendantTwo.ancestor
    else:
        difference = depthOne - depthTwo
        for i in range(difference):
            descendantOne = descendantOne.ancestor

    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    
    return descendantOne
