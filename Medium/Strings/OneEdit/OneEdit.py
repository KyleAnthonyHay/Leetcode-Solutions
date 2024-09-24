# Time O(n) | Space O(1)
def oneEdit(stringOne, stringTwo):
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)
    if abs(lengthOne - lengthTwo) > 1:
        return False

    madeEdit = False
    indexOne, indexTwo = 0, 0

    while indexOne < lengthOne and indexTwo < lengthTwo:
        if stringOne[indexOne] != stringTwo[indexTwo]:
            if madeEdit:
                return False
            madeEdit = True

            if lengthOne > lengthTwo:
                indexOne += 1
            elif lengthOne < lengthTwo:           
                indexTwo += 1
            else:
                indexOne += 1
                indexTwo += 1
        else:
            indexOne += 1
            indexTwo += 1

    return True