# Non-Optimal Solution
def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        if array[left] == target:
            return left
        if array[right] == target:
            return right
        elif array[left] < target:
            left += 1
        elif array[right] > target:
            right -= 1
    return -1


# Optimal Solution
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
    return -1


# Recursive Solution
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    if target == array[middle]:
        return middle
    elif target > array[middle]:
        return binarySearchHelper(array, target, middle + 1, right)
    else:
        return binarySearchHelper(array, target, left, middle - 1)
