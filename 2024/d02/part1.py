# https://adventofcode.com/2024/day/2

lines = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

f = open('data', 'r')
lines = f.read()

def isSafe(report):
    print(report)
    diffs = [(report[i+1] - report[i]) for i in range(len(report)-1)]
    print(diffs)
    if diffs[0] < 1:
        for d in diffs:
            if d > -1:
                return False
            if d < -3:
                return False
        return True
    else:
        for d in diffs:
            if d < 1:
                return False
            if d > 3:
                return False
        return True

safe = 0
for line in lines.split('\n'):
    if not line:
        continue
    report = [int(level) for level in line.split(' ')]
    if isSafe(report):
        safe += 1

print(safe)
