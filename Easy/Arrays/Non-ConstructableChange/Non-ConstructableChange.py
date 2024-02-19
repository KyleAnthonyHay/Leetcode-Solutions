# Optimal Solution
# Time: O(nlogn)
# Space: O(1)

def nonConstructibleChange(coins):
    coins.sort()
    change = 0

    for coin in coins:
        if coin > change + 1:
            break
        change += coin

    return change + 1
