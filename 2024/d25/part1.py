# https://adventofcode.com/2024/day/25

import numpy as np

input = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

def makeGrid(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h,w), '.')
    for i in range(h):
        for j in range(w):
            grid[i, j] = lines[i][j]
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

def parseInput(input):
    locks = []
    keys  = []
    blocks = input.split('\n\n')
    print(len(blocks))
    for block in blocks:
        grid = makeGrid(block)
        printGrid(grid)
        print()
        h, w = grid.shape
        heights = []
        for c in range(w):
            heights.append(np.count_nonzero(grid[:,c] == '#')-1)
        print(heights)
        if grid[0, 0] == '#':
            locks.append(heights)
        else:
            keys.append(heights)

    return locks, keys

input = open('data', 'r').read()
locks, keys = parseInput(input)
print(locks)
print(keys)

total = 0
for lock in locks:
    for key in keys:
        print(lock, key)
        fits = True
        for i in range(len(lock)):
            if lock[i] + key[i] > 5:
                fits = False
                break
        if fits:
            total += 1
print(total)
