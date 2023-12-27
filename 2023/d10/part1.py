# https://adventofcode.com/2023/day/10

import numpy as np

data = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

data = open('data', 'r').read()

def makeGrid(input):
    lines = input.strip().split('\n')
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h+2,w+2), '.')
    for i in range(h):
        for j in range(w):
            grid[i+1,j+1] = lines[i][j]
    return grid

grid = makeGrid(data)
print(grid)
loc = np.where(grid == 'S')
row, col = loc[0][0], loc[1][0]
print(row, col)

moves = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

pipes = {
    '|': { 'N': 'N', 'S': 'S' },
    '-': { 'E': 'E', 'W': 'W' },
    'L': { 'S': 'E', 'W': 'N' },
    'J': { 'S': 'W', 'E': 'N' },
    '7': { 'E': 'S', 'N': 'W' },
    'F': { 'W': 'S', 'N': 'E' },
}

direction = 'E'

steps = 0
while True:
    dr, dc = moves[direction]
    row += dr
    col += dc
    cell = grid[row,col]
    print(direction, row, col, cell)
    if cell == 'S':
        break
    direction = pipes[cell][direction]
    steps += 1

print(steps)
print((steps+1)//2)
