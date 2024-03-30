# Optimal Solution

def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
