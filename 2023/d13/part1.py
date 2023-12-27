# https://adventofcode.com/2023/day/13

import numpy as np

data = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

def makeGrid(input):
    lines = input.strip().split('\n')
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h,w), '.')
    for i in range(h):
        for j in range(w):
            grid[i,j] = lines[i][j]
    return grid

def printGrid(grid):
    for row in grid:
        print("".join(list(row)))

def parse(data):
    patterns = []
    grids = data.strip().split('\n\n')
    for grid in grids:
        pattern = makeGrid(grid)
        patterns.append(pattern)
    return patterns

def hcheck(pattern, row, h):
    other = row
    for r in range(row+1, h):
        if other < 0:
            break
        if not np.all(pattern[r] == pattern[other]):
            return False
        other = other - 1
    return True

def hreflection(pattern):
    h, w = pattern.shape
    for row in range(h-1):
        #print(row, pattern[row])
        if np.all(pattern[row] == pattern[row+1]):
            if hcheck(pattern, row, h):
                return row+1
    return 0

def vcheck(pattern, col, w):
    other = col
    for c in range(col+1, w):
        if other < 0:
            break
        if not np.all(pattern[:,c] == pattern[:,other]):
            return False
        other = other - 1
    return True

def vreflection(pattern):
    h, w = pattern.shape
    for col in range(w-1):
        #print(col, pattern[:,col])
        if np.all(pattern[:,col] == pattern[:,col+1]):
            if vcheck(pattern, col, w):
                return col+1
    return 0

data = open('data', 'r').read()

tv = 0
th = 0
patterns = parse(data)
for pattern in patterns:
    print(pattern.shape)
    printGrid(pattern)
    x = hreflection(pattern)
    print(f"hreflection = {x}")
    th += x
    y = vreflection(pattern)
    print(f"vreflection = {y}")
    tv += y

print(th, tv, 100*th + tv)
