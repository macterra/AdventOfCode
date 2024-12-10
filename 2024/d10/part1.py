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

test1 = """
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
"""

test2 = """
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
"""

#input = test2

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

def search(grid, score, i, j):
    alt = grid[i, j]

    if alt == 9:
        score[i, j] = 'X'
        return

    if grid[i-1, j] == alt+1:
        search(grid, score, i-1, j)
    if grid[i+1, j] == alt+1:
        search(grid, score, i+1, j)
    if grid[i, j-1] == alt+1:
        search(grid, score, i, j-1)
    if grid[i, j+1] == alt+1:
        search(grid, score, i, j+1)

grid = makeGrid(input)
printGrid(grid)

h, w = grid.shape

ys, xs = np.where(grid == 0)
trailheads = list(zip(ys, xs))
print(trailheads)

total = 0
for i, j in trailheads:
    score = np.full((h, w), '.')
    search(grid, score, i, j)
    s = np.count_nonzero(score == 'X')
    print(i, j, s)
    total += s
print(total)
