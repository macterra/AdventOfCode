# https://adventofcode.com/2024/day/6

import numpy as np

input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

input = open('data', 'r').read()

def makeGrid(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h+2,w+2), ' ')
    for i in range(h):
        for j in range(w):
            grid[i+1,j+1] = lines[i][j]
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()


grid = makeGrid(input)
print(grid)
guard = '^'
pos = np.where(grid == guard)
i, j = pos[0][0], pos[1][0]

print(i, j)
print(grid)

while True:
    grid[i, j] = 'X'
    if guard == '^':
        look = grid[i-1, j]
        if look == ' ':
            break
        elif look != '#':
            i -= 1
        else:
            guard = '>'
    if guard == '>':
        look = grid[i, j+1]
        if look == ' ':
            break
        elif look != '#':
            j += 1
        else:
            guard = 'v'
    if guard == 'v':
        look = grid[i+1, j]
        if look == ' ':
            break
        elif look != '#':
            i += 1
        else:
            guard = '<'
    if guard == '<':
        look = grid[i, j-1]
        if look == ' ':
            break
        elif look != '#':
            j -= 1
        else:
            guard = '^'
    grid[i, j] = guard
    #printGrid(grid)

grid[i, j] = 'X'
printGrid(grid)

num = np.count_nonzero(grid == 'X')
print(num)
