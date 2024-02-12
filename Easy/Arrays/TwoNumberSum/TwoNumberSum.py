def twoNumberSum(array, targetSum):
    previouslyFoundNumbers = {}

    for num in array:
        potentialAddend = targetSum - num
        if potentialAddend in previouslyFoundNumbers:
            return [num, potentialAddend]
        else:
            previouslyFoundNumbers[num] = True

    return []
