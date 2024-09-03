# Optimal Solution

# Time 0(n) | Space 0(n)
def zeroSumSubarray(nums):
    sums = set([0])
    currentSum = 0

    for num in nums:
        currentSum = currentSum + num
        if currentSum in sums:
            return True
        else:
            sums.add(currentSum)
    
    return False



