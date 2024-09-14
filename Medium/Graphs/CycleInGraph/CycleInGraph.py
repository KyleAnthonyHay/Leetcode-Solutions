# Time O(V + E) | Space O(V)
def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if visited[node]:
            continue
            
        containsCycle = isNodeInCycle(edges, node, visited, currentlyInStack)
        if containsCycle:
            return True
            
    return False

def isNodeInCycle(edges, node, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True
    neighbors = edges[node]
    
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(edges, neighbor, visited, currentlyInStack)
            if containsCycle:
                return True
        elif currentlyInStack[neighbor]:
            return True

    currentlyInStack[node] = False
    return False