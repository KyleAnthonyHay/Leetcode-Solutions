# Optimal Solution

def runLengthEncoding(string):
    result = []
    count = 1

    for idx in range(len(string) - 1):
        if string[idx] == string[idx + 1] and count < 9:
            count += 1
        else:
            result.append(str(count))
            result.append(string[idx])
            count = 1

    result.append(str(count))
    result.append(string[-1])

    return "".join(result)
