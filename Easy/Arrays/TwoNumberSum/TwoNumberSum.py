# Solution 1 Time Complexity: O(n) Space Complexity: O(n)
def twoNumberSum(array, targetSum):
    previouslyFoundNumbers = {}

    for num in array:
        potentialAddend = targetSum - num
        if potentialAddend in previouslyFoundNumbers:
            return [num, potentialAddend]
        else:
            previouslyFoundNumbers[num] = True

    return []

# Solution 1 Time Complexity: O(nlogn) WORST? Space Complexity: O(1)


def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum > targetSum:
            right -= 1
        elif currentSum < targetSum:
            left += 1
    return []
