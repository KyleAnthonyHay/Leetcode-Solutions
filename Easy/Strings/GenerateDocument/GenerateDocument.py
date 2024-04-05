# Optimal Solution

def generateDocument(characters, document):
    chars = {}

    # Count Character Occourences in characters
    for char in characters:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    # Subtract Character Occourences from characters
    for char in document:
        if char not in chars or chars[char] == 0:
            return False
        else:
            chars[char] -= 1

    return True
