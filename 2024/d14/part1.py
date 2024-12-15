# https://adventofcode.com/2024/day/14

import re

input = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

input = open('data', 'r').read()

def parseInput(input):
    robots = []
    lines = [line for line in input.split('\n') if line.strip() != '']
    for line in lines:
        match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        x, y, vx, vy = match.group(1), match.group(2), match.group(3), match.group(4)
        robots.append((int(x), int(y), int(vx), int(vy)))
    return robots

width = 101
midw = width//2
height = 103
midh = height//2
t = 100

robots = parseInput(input)
quadrants = { "NW": 0, "NE": 0, "SW": 0, "SE": 0 }
for robot in robots:
    x, y, vx, vy = robot
    fx, fy = (x + vx * t) % width, (y + vy * t) % height
    print(fx, fy)
    if fx == midw or fy == midh:
        continue
    if fx < midw and fy < midh:
        q = "NW"
    elif fx > midw and fy < midh:
        q = "NE"
    elif fx < midw and fy > midh:
        q = "SW"
    elif fx > midw and fy > midh:
        q = "SE"
    else:
        print("oops")
    print(fx, fy, q)
    quadrants[q] += 1

print(quadrants)
print(quadrants["NE"] * quadrants["NW"] * quadrants["SE"] * quadrants["SW"])
