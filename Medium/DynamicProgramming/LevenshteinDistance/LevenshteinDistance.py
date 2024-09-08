# Optimal Solution

# Time 0(n) | Space 0(1)
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    prevMax = array[0]
    currentMax = max(array[0], array[1])

    for i in range(2, len(array)):
        newMax = max(currentMax, prevMax + array[i])
        prevMax = currentMax
        currentMax = newMax
    
    return currentMax
