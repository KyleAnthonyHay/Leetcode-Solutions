# Optimal Solution

def firstNonRepeatingCharacter(string):
    occurences = {}
    for char in string:
        if char not in occurences:
            occurences[char] = 1
        else:
            occurences[char] += 1

    for idx, char in enumerate(string):
        if occurences[char] == 1:
            return idx

    return -1
