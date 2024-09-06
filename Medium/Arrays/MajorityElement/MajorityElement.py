# Optimal Solution

# Time 0(n) | Space 0(1)
def majorityElement(array):
    count = 0
    answer = None
    
    for num in array:
        if count == 0:
            answer = num

        if num == answer:
            count += 1
        else:
            count -= 1
            
    return answer
