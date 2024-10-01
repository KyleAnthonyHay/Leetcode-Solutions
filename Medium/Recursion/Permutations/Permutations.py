# Time O(n) | Space O(n! * n)
def getPermutations(array):
    permuations = []
    permuationsHelper(0, array, permuations)
    return permuations

def  permuationsHelper(i, array, permuations):
    if i == len(array) - 1:
        permuations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permuationsHelper(i + 1, array, permuations)
            swap(array, i, j)
            
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]