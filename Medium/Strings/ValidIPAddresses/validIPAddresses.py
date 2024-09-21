# Time O(1) | Space O(1)
def validIPAddresses(string):
    ipAddressesFound = []

    for i in range(1, min(len(string), 4)):
        currentIPAddressParts = ['', '', '', '']

        currentIPAddressParts[0] = string[:i]
        if not isValid(currentIPAddressParts[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIPAddressParts[1] = string[i: j]
            if not isValid(currentIPAddressParts[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)): 
                currentIPAddressParts[2] = string[j: k]
                currentIPAddressParts[3] = string[k:]
                if isValid(currentIPAddressParts[2]) and isValid(currentIPAddressParts[3]):
                    ipAddressesFound.append('.'.join(currentIPAddressParts))
                    
        
    return ipAddressesFound


def isValid(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False

    return len(string) == len(str(stringAsInt)) # check for leading 0