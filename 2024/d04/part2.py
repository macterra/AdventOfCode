# https://adventofcode.com/2024/day/4

import numpy as np

input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

input = open('data', 'r').read()

def makeGrid(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h+6,w+6), '.')
    for i in range(h):
        for j in range(w):
            grid[i+3,j+3] = lines[i][j]
    return grid

def checkXmas(grid, i, j):
    if (grid[i-1,j-1] == 'M' and grid[i+1,j+1] == 'S') or (grid[i-1,j-1] == 'S' and grid[i+1,j+1] == 'M'):
        if (grid[i+1,j-1] == 'M' and grid[i-1,j+1] == 'S') or (grid[i+1,j-1] == 'S' and grid[i-1,j+1] == 'M'):
            return 1
    return 0

grid = makeGrid(input)
print(grid)

h, w = grid.shape
print(h, w)
total = 0
for i in range(h):
    for j in range(w):
        if grid[i,j] == 'A':
            total += checkXmas(grid, i, j)
print(total)
