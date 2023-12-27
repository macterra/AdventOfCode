# https://adventofcode.com/2023/day/14

import numpy as np

data = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
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

def moveRocks(grid):
    h, w = grid.shape
    moved = 0
    for row in range(1,h):
        for col in range(w):
            if grid[row,col] == 'O' and grid[row-1,col] == '.':
                grid[row, col], grid[row-1,col] = '.', 'O'
                moved += 1
    return moved

def tilt(grid):
    while True:
        if not moveRocks(grid):
            break

def calcLoad(grid):
    h, w = grid.shape
    load = 0
    for row in range(h):
        load += (h-row) * np.where(grid[row] == 'O')[0].size
    return load

data = open('data', 'r').read()
grid = makeGrid(data)

printGrid(grid)
tilt(grid)
printGrid(grid)
print(calcLoad(grid))

