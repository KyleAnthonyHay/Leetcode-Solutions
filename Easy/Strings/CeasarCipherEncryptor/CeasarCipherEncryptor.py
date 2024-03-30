# Optimal Solution

def caesarCipherEncryptor(string, key):
    shiftValue = key % 26
    newString = ""
    for char in string:
        unicodeValue = ord(char) + shiftValue
        if unicodeValue <= 122:
            newString += chr(unicodeValue)
        else:
            newString += chr(96 + unicodeValue % 122)
    return newString
