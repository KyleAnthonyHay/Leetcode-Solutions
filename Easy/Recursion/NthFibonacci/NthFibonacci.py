# Optimal Solution

def productSum(array, depth=1):
    sum = 0
    for value in array:
        if type(value) is list:
            sum += productSum(value, depth + 1)
        else:
            sum += value
    return sum * depth
