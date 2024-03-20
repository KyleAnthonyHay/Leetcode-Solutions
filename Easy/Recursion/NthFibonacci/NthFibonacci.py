# Optimal Solution

# Bad Recursive Solution O(2^n) Time | O(n) Space
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)

# Better Recursive Solution O(n) Time | O(n) Space


def getNthFib(n, memorize={1: 0, 2: 1}):
    # Write your code here.
    if n in memorize:
        return memorize[n]
    else:
        memorize[n] = getNthFib(n-1, memorize) + getNthFib(n-2, memorize)
        return memorize[n]

# Optimal Solutiondef getNthFib(n):


def getNthFib(n):
    # Base Case Values
    a = 0
    b = 1

    for _ in range(n-1):
        temp = a
        a = b
        b += temp
    return a
