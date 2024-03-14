# Optimal Solution

def minimumWaitingTime(queries):
    queries.sort()
    minimumWaitingTime = 0

    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        minimumWaitingTime += duration * queriesLeft

    return minimumWaitingTime
