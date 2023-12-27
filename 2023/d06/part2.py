# https://adventofcode.com/2023/day/6

input = """
Time:      7  15   30
Distance:  9  40  200
"""

race = (71530, 940200)

puzzle = """
Time:        49     97     94     94
Distance:   263   1532   1378   1851
"""

race = (49979494, 263153213781851)

time, dist = race
print(race)

for t in range(0, time):
    d = (time-t) * t
    if d > dist:
        print(t)
        a = t
        break

for t in range(time-1, 0, -1):
    d = (time-t) * t
    if d > dist:
        print(t)
        b = t
        break

print(a, b)
print(b - a + 1)
