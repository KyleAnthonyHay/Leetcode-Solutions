# Time O(W * Nlog(n)) | Space O(WN)
def groupAnagrams(words):
    anagrams = {} # hashtable
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())