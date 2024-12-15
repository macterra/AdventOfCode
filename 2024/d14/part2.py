# https://adventofcode.com/2024/day/14

import re
import numpy as np
import zlib

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
height = 103

robots = parseInput(input)

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

def compressibility(grid):
    # Convert grid to a single string
    lines = ["".join(row) for row in grid]
    raw_data = "\n".join(lines).encode('utf-8')  # encode to bytes
    compressed = zlib.compress(raw_data, level=9)
    ratio = len(compressed) / len(raw_data)
    return ratio

t = 0
while True:
    grid = np.full((height, width), '.')
    for robot in robots:
        x, y, vx, vy = robot
        fx, fy = (x + vx * t) % width, (y + vy * t) % height
        grid[fy, fx] = '*'
    if t%1000 == 0:
        print(t)
    c = compressibility(grid)
    if c < 0.05:
        printGrid(grid)
        print(t, c)
        break
    t += 1
