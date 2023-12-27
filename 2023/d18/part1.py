# https://adventofcode.com/2023/day/18

import numpy as np

data = r"""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

data = open('data', 'r').read()

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
    plan = []
    for line in data.strip().split('\n'):
        d, n, color = line.split(' ')
        plan.append((d, int(n)))
    return plan

def dig(plan):
    trench = []
    row = 0
    col = 0
    for d, n in plan:
        for i in range(n):
            if d == 'U':
                row -= 1
            if d == 'D':
                row += 1
            if d == 'L':
                col -= 1
            if d == 'R':
                col += 1
            trench.append((row, col))
    return trench

def makeLagoon(trench):
    minrow = min([row for row, col in trench])
    mincol = min([col for row, col in trench])
    maxrow = max([row for row, col in trench])
    maxcol = max([col for row, col in trench])

    print(minrow, mincol, maxrow, maxcol)

    width = maxcol - mincol + 1
    height = maxrow - minrow + 1

    grid = np.full((height, width), '.')
    for row, col in trench:
        grid[row - minrow, col - mincol] = '#'

    return grid

def flood(grid):
    visited = set()
    rows, cols = grid.shape

    row = 0
    col = 0

    while grid[row, col] == '.':
        col += 1

    row += 1

    while grid[row, col] == '#':
        col += 1

    queue = [(row, col)]

    while queue:
        loc = queue.pop(0)

        if loc not in visited:
            visited.add(loc)
            row, col = loc
            if grid[row, col] == '.':
                grid[row, col] = 'o'

                if row > 0:
                    queue.append((row-1, col))
                if row < (rows-1):
                    queue.append((row+1, col))
                if col > 0:
                    queue.append((row, col-1))
                if col < (cols-1):
                    queue.append((row, col+1))

plan = parse(data)
print(plan)

trench = dig(plan)
print(trench)

lagoon = makeLagoon(trench)
printGrid(lagoon)

flood(lagoon)
print()
printGrid(lagoon)

print(np.count_nonzero(lagoon != '.'))
