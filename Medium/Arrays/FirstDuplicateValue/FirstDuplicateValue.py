# Optimal Solution

# Time 0(n) | Space 0(1)
def firstDuplicateValue(array):
    
    for num in array:
        absolutevalue = abs(num) 
        if array[absolutevalue - 1] < 0:
            return absolutevalue
        else:
            array[absolutevalue - 1] *= - 1
            
    return -1