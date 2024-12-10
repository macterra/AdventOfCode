# https://adventofcode.com/2024/day/10

import numpy as np

input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

input = open('data', 'r').read()

def makeGrid(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h+2,w+2), -1)
    for i in range(h):
        for j in range(w):
            if lines[i][j] == '.':
                grid[i+1,j+1] = -1
            else:
                grid[i+1,j+1] = int(lines[i][j])
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            if cell < 0:
                print('.', end='')
            else:
                print(cell, end='')
        print()

def search(grid, i, j):
    alt = grid[i, j]

    if alt == 9:
        return 1

    rating = 0
    if grid[i-1, j] == alt+1:
        rating += search(grid, i-1, j)
    if grid[i+1, j] == alt+1:
        rating += search(grid, i+1, j)
    if grid[i, j-1] == alt+1:
        rating += search(grid, i, j-1)
    if grid[i, j+1] == alt+1:
        rating += search(grid, i, j+1)

    return rating

grid = makeGrid(input)
printGrid(grid)

h, w = grid.shape

ys, xs = np.where(grid == 0)
trailheads = list(zip(ys, xs))
print(trailheads)

total = 0
for i, j in trailheads:
    rating = search(grid, i, j)
    print(i, j, rating)
    total += rating
print(total)
