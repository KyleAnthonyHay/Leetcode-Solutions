# Optimal Solution

# Time 0(n) | Space 0(1)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
            else:
                continue

    return ways[-1]
