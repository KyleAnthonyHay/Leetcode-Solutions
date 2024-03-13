# Optimal Solution

def optimalFreelancing(jobs):
    DaysOfTheWeek = 7
    profit = 0
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    timeline = [False] * DaysOfTheWeek

    for job in jobs:
        maxTime = min(job["deadline"], DaysOfTheWeek)
        for time in reversed(range(maxTime)):
            if timeline[time] == False:
                timeline[time] = True
                profit += job["payment"]
                break

    return profit
