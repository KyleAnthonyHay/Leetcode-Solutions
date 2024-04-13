# Optimal Solution

def smallestDifference(arrayOne, arrayTwo):
    result = []
    smallestDifference = float('inf')
    currentDifference = float('inf')
    arrayOne.sort()
    arrayTwo.sort()
    p1 = 0
    p2 = 0

    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        firstNum, secondNum = arrayOne[p1], arrayTwo[p2]
        if firstNum == secondNum:
            return [firstNum, secondNum]
        if firstNum < secondNum:
            currentDifference = secondNum - firstNum
            p1 += 1
        elif arrayOne[p1] > arrayTwo[p2]:
            currentDifference = firstNum - secondNum
            p2 += 1
        if currentDifference < smallestDifference:
            smallestDifference = currentDifference
            result = [firstNum, secondNum]

    return result
