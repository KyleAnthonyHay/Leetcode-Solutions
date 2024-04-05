# Optimal Solution

def commonCharacters(strings):
    charCount = {}

    for string in strings:
        uniqueChars = set(string)
        for char in uniqueChars:
            if char not in charCount:
                charCount[char] = 0
            charCount[char] += 1

    finalCharacters = []
    for char, count in charCount.items():
        if count == len(strings):
            finalCharacters.append(char)

    return finalCharacters
