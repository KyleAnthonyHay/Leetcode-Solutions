# Time 0(V+E) | Space 0(V)
def breadthFirstSearch(self, array):
    queue = [self]
    while len(queue) > 0:
        current = queue.pop(0)
        array.append(current.name)
        for child in current.children:
            queue.append(child)
            
    return array