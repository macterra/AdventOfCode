# https://adventofcode.com/2025/day/1

lines = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

f = open('data', 'r')
lines = f.read()

rotations = []
dial = 50
zeros = 0

for line in lines.split('\n'):
    if not line:
        continue
    rotations.append(line)

print(rotations)

for rotation in rotations:
    direction = rotation[0]
    steps = int(rotation[1:])

    if direction == 'L':
        for i in range(steps):
            dial -= 1
            dial %= 100
            if dial == 0:
                zeros += 1
    else:
        for i in range(steps):
            dial += 1
            dial %= 100
            if dial == 0:
                zeros += 1

    print(direction, steps, dial)

print("Number of times dial hits zero:", zeros)
