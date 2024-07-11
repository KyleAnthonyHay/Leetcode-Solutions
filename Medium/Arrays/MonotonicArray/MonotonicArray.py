# Optimal Solution

# Time 0(n) | Space O(1)
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True

    for idx in range(1, len(array)):
        if array[idx - 1] < array[idx]:
            isNonIncreasing = False
        if array[idx - 1] > array[idx]:
            isNonDecreasing = False
        
    return isNonDecreasing or isNonIncreasing

