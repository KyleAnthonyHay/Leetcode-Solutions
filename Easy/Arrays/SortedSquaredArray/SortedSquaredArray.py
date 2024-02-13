# Optimal Solution
# Time: O(n)
# Space: O(n)

def sortedSquaredArray(array):
    newArray = [0 for _ in array]
    start = 0
    end = len(array) - 1
    newArrayPointer = len(newArray) - 1

    while start <= end:
        if abs(array[start]) < abs(array[end]):
            newArray[newArrayPointer] = array[end] ** 2
            end -= 1
            newArrayPointer -= 1
        else:
            newArray[newArrayPointer] = array[start] ** 2
            start += 1
            newArrayPointer -= 1

    return newArray


# Non-Optimal Solution
# Time: O(nlogn + n)sorting + squaring
# Space: O(n)
def sortedSquaredArray(array):
    newArray = []
    for idx, num in enumerate(array):
        newArray.append(num * num)
    newArray.sort()
    return newArray
