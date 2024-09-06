# Optimal Solution

# Time 0(nlog(n)) | Space 0(n)
def sweetAndSavory(dishes, target):
    dishes.sort()
    left = 0
    right = len(dishes) - 1
    result = [0, 0]
    bestMatch = float('inf')
    

    while left < right:
        if dishes[right] < 0 or dishes[left] > 0:
            break
            
        potentialMatch = dishes[left] + dishes[right]
        if potentialMatch > target:
            right -= 1
        else:    
            if target - potentialMatch < bestMatch:
                result = [dishes[left], dishes[right]]
                bestMatch = target - potentialMatch
            left += 1
            
    return result
