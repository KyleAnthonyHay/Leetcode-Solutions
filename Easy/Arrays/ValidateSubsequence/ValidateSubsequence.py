def isValidSubsequence(array, sequence):
    # initial check to save unnessecary calculations
    if len(array) < len(sequence):
        return False

    seqPointer = 0
    for value in array:
        if value == sequence[seqPointer]:
            seqPointer += 1
        if seqPointer == len(sequence):
            return True

    return False
