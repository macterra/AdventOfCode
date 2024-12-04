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
    n = 0
    if grid[i+0,j+0] == 'X' and grid[i,j+1] == 'M' and grid[i,j+2] == 'A' and grid[i,j+3] == 'S':
        n += 1 # east
    if grid[i+0,j+0] == 'X' and grid[i,j-1] == 'M' and grid[i,j-2] == 'A' and grid[i,j-3] == 'S':
        n += 1 # west
    if grid[i+0,j+0] == 'X' and grid[i+1,j] == 'M' and grid[i+2,j] == 'A' and grid[i+3,j] == 'S':
        n += 1 # south
    if grid[i+0,j+0] == 'X' and grid[i-1,j] == 'M' and grid[i-2,j] == 'A' and grid[i-3,j] == 'S':
        n += 1 # north
    if grid[i+0,j+0] == 'X' and grid[i+1,j+1] == 'M' and grid[i+2,j+2] == 'A' and grid[i+3,j+3] == 'S':
        n += 1 # SE
    if grid[i+0,j+0] == 'X' and grid[i-1,j-1] == 'M' and grid[i-2,j-2] == 'A' and grid[i-3,j-3] == 'S':
        n += 1 # NW
    if grid[i+0,j+0] == 'X' and grid[i-1,j+1] == 'M' and grid[i-2,j+2] == 'A' and grid[i-3,j+3] == 'S':
        n += 1 # NE
    if grid[i+0,j+0] == 'X' and grid[i+1,j-1] == 'M' and grid[i+2,j-2] == 'A' and grid[i+3,j-3] == 'S':
        n += 1 # SW
    return n

grid = makeGrid(input)
print(grid)

h, w = grid.shape
print(h, w)
total = 0
for i in range(h):
    for j in range(w):
        if grid[i,j] == 'X':
            print(i, j, grid[i,j])
            total += checkXmas(grid, i, j)
print(total)
