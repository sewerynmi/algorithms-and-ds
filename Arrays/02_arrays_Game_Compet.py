# Desc:
# There is a turnament. Games (round robin style) array: ["home","away"]
# [
#   ["HTML", "C#"],
#   ["C#", "Python"],
#   ["Python", "HTML"]
# ]
# and results = [0,0,1]
# O is when "away" team wins, 1 if "home" team wins.
# 3 point for win. The turnament winner is a team

def tournamentWinner(comptetitions, results):
    cuurentBestTeam = ""
    scores = {cuurentBestTeam: 0}
    for idx, competition in enumerate(comptetitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        # Set winning team (home = 1)
        winningTeam = homeTeam if result == 1 else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[cuurentBestTeam]:
            cuurentBestTeam = winningTeam

    return cuurentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points


# TEST
competitions = [
    ["C#", "HTML"],
    ["HTML", "Python"],
    ["Python", "C#"]
]
scores = [0, 0, 1]
print(tournamentWinner(competitions, scores))
