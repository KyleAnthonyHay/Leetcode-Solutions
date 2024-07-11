# Optimal Solution

# Time 0(n) | Space 0(1)
def moveElementToEnd(array, toMove):
    first = 0
    last = len(array) - 1

    while first < last:
        while first < last and array[last] == toMove:
            last -= 1
        if array[first] == toMove:
            array[first], array[last] = array[last], array[first]
        first += 1
    return array
