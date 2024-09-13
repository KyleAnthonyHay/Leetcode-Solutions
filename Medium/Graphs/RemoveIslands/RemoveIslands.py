# Time O(D) | Space O(1)

def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue
            if matrix[row][col] != 1:
                continue
                
            changeOnesConnectedToBorderToTwos(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            color = matrix[row][col]
            if color == 1:
                matrix[row][col] = 0
            elif color == 2:
                matrix[row][col] = 1
            
    return matrix

def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition
        
        matrix[currentRow][currentCol] = 2
        
        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor
            
            if matrix[row][col] != 1:
                continue
                
            stack.append(neighbor)

def getNeighbors(matrix, row, col):
    neighbors = []

    numRows = len(matrix)
    numCols = len(matrix[row])
    
    if row - 1 >= 0: # Up
        neighbors.append((row - 1, col))
    if row + 1 < numRows: # Down
        neighbors.append((row + 1, col))
    if col - 1 >= 0: # left
        neighbors.append((row, col - 1))
    if col + 1 < numCols: # right
        neighbors.append((row, col + 1))
    return neighbors