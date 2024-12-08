# https://adventofcode.com/2024/day/8

import numpy as np
import string

input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

input = open('data', 'r').read()

def makeGrid(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h,w), '.')
    for i in range(h):
        for j in range(w):
            grid[i,j] = lines[i][j]
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

def addAntinodes(grid, char, coords):
    n = len(coords)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(char, coords[i], coords[j])
            i1, j1 = coords[i]
            i2, j2 = coords[j]
            di = i2 - i1
            dj = j2 - j1

            a, b = i1, j1
            while addAntinode(grid, a, b):
                a += di
                b += dj

            a, b = i1, j1
            while addAntinode(grid, a, b):
                a -= di
                b -= dj

def addAntinode(grid, i, j):
    h, w = grid.shape
    if i < 0 or j < 0:
        return False
    if i >= h or j >= w:
        return False
    grid[i, j] = '#'
    return True

grid = makeGrid(input)
printGrid(grid)

h, w = grid.shape
grid2 = np.full((h,w), '.')

characters = string.digits + string.ascii_lowercase + string.ascii_uppercase
for char in characters:
    ys, xs = np.where(grid == char)
    if ys.size > 0:
        print(char, list(zip(ys, xs)))
        addAntinodes(grid2, char, list(zip(ys, xs)))

printGrid(grid2)
print(np.count_nonzero(grid2 == '#'))
