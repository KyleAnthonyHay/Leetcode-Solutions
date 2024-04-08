# Optimal Solution

def semordnilap(words):
    wordsSet = set(words)
    pairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word:
            pairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)

    return pairs
