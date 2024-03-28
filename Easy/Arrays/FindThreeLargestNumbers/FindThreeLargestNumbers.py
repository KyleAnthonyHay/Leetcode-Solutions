# Optimal Solution

def findThreeLargestNumbers(array):
    threeLargest = [None] * 3

    for num in array:
        if threeLargest[2] is None or num > threeLargest[2]:
            shiftAndUpdate(threeLargest, num, 2)
        elif threeLargest[1] is None or num > threeLargest[1]:
            shiftAndUpdate(threeLargest, num, 1)
        elif threeLargest[0] is None or num > threeLargest[0]:
            shiftAndUpdate(threeLargest, num, 0)
    return threeLargest


def shiftAndUpdate(array, num, Targetidx):
    for i in range(Targetidx + 1):
        if i == Targetidx:
            array[i] = num
        else:
            array[i] = array[i+1]
