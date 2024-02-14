# Optimal Solution
# Time: O(n) Number of Tournaments
# Space: O(k) Number of Teams

def tournamentWinner(competitions, results):
    champion = ""
    scores = {"": 0}

    for idx, competition in enumerate(competitions):
        if results[idx] == 1:
            winningTeam = competition[0]
        else:
            winningTeam = competition[1]
        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[champion]:
            champion = winningTeam
    return champion


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
