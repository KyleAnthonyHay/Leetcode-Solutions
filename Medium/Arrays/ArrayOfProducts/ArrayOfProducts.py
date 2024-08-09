# Optimal Solution

# Time 0(n) | Space 0(n)
def arrayOfProducts(array):
    newArray = [1 for _ in range(len(array))]
    
    accumilatedProduct = 1
    for i in range(len(array)):
        newArray[i] = accumilatedProduct
        accumilatedProduct *= array[i]

    accumilatedProduct = 1
    for i in reversed(range(len(array))):
        newArray[i] *= accumilatedProduct
        accumilatedProduct *= array[i]
        
    return newArray
