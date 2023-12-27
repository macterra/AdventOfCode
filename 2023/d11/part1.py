# https://adventofcode.com/2023/day/11

import numpy as np

data = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
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

def expandSpace(grid):
    h, w = grid.shape
    for row in reversed(range(h)):
        if np.all(grid[row] == '.'):
            grid = np.insert(grid, row, grid[row], axis=0)

    for col in reversed(range(w)):
        if np.all(grid[:,col] == '.'):
            grid = np.insert(grid, col, grid[:,col], axis=1)

    return grid

grid = makeGrid(data)
grid = expandSpace(grid)

loc = np.where(grid != '.')
galaxies = list(zip(*loc))

def shortestPath(galaxy, galaxies):
    dist = 0
    r1, c1 = galaxy
    for r2, c2 in galaxies:
        dist += abs(r1-r2) + abs(c1-c2)
    return dist

sum = 0
for i in range(0, len(galaxies)-1):
    sum += shortestPath(galaxies[i], galaxies[i+1:])

print(sum)
