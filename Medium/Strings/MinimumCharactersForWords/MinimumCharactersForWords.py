# Time O(n * l) | Space O(C)
def minimumCharactersForWords(words):
    mainMap = {}
    resultList = []
    for word in words:
        tempMap = {}
        for letter in word:
            if letter not in mainMap:
                mainMap[letter] = 1
                resultList.append(letter)
            tempMap[letter] = tempMap.get(letter, 0) + 1
            if tempMap[letter] > mainMap[letter]:
                resultList.append(letter)
                mainMap[letter] += 1
    return resultList
