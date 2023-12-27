# https://adventofcode.com/2023/day/6

input = """
Time:      7  15   30
Distance:  9  40  200
"""

races = ((7, 9), (15, 40), (30, 200))

puzzle = """
Time:        49     97     94     94
Distance:   263   1532   1378   1851
"""

races = ((49, 263), (97, 1532), (94, 1378), (94, 1851))

ways = 1
for race in races:
    time, dist = race
    print(race)
    distances = []
    wins = 0
    for t in range(0, time):
        d = (time-t) * t
        distances.append(d)
        if d > dist:
            wins += 1
    print(distances)
    print(wins)
    ways *= wins
print(ways)

