# Optimal Solution

# Time 0(n) | Space 0(n)
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1): 
            result.append(array[startRow][col])
            
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
            
        if startRow < endRow:
            for col in reversed(range(startCol, endCol)):
                result.append(array[endRow][col])
        if startCol < endCol: 
            for row in reversed(range(startRow + 1, endRow)):
                 result.append(array[row][startCol])
            
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
        
    return result
