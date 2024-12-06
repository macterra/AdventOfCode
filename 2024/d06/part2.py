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

test1 = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#.#^.....
........#.
#.........
......#...
"""

test2 = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
......#.#.
#.........
......#...
"""

#input = test2
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

def simulate(grid):
    guard = '^'
    pos = np.where(grid == guard)
    i, j = pos[0][0], pos[1][0]

    tracks = { '^': [], '>': [], 'v': [], '<': [] }

    #print(i, j)
    #printGrid(grid)

    while True:
        if (i,j) in tracks[guard]:
            return True

        tracks[guard].append((i,j))

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

    #printGrid(grid)
    #print(tracks)

    return False

grid = makeGrid(input)

guard = '^'
pos = np.where(grid == guard)
y, x = pos[0][0], pos[1][0]

h, w = grid.shape
print(h, w)
total = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if i == y and j == x:
            continue
        test = grid.copy()
        test[i,j] = '#'
        if simulate(test):
            total += 1
        print(i, j, total)
print(total)
