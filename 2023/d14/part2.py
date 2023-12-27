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

def moveRocks(grid, direction):
    h, w = grid.shape
    moved = 0

    if direction == 'N':
        for row in range(1,h):
            for col in range(w):
                if grid[row,col] == 'O' and grid[row-1,col] == '.':
                    grid[row, col], grid[row-1,col] = '.', 'O'
                    moved += 1

    if direction == 'S':
        for row in range(h-2,-1,-1):
            for col in range(w):
                if grid[row,col] == 'O' and grid[row+1,col] == '.':
                    grid[row, col], grid[row+1,col] = '.', 'O'
                    moved += 1

    if direction == 'W':
        for col in range(1,w):
            for row in range(h):
                if grid[row,col] == 'O' and grid[row,col-1] == '.':
                    grid[row, col], grid[row,col-1] = '.', 'O'
                    moved += 1

    if direction == 'E':
        for col in range(w-2,-1,-1):
            for row in range(h):
                if grid[row,col] == 'O' and grid[row,col+1] == '.':
                    grid[row, col], grid[row,col+1] = '.', 'O'
                    moved += 1

    return moved

def spinCycle(grid):
    while True:
        if not moveRocks(grid, 'N'):
            break
    while True:
        if not moveRocks(grid, 'W'):
            break
    while True:
        if not moveRocks(grid, 'S'):
            break
    while True:
        if not moveRocks(grid, 'E'):
            break

def calcLoad(grid):
    h, w = grid.shape
    load = 0
    for row in range(h):
        load += (h-row) * np.where(grid[row] == 'O')[0].size
    return load

def findTarget(seq, target):
    targetLen = len(target)
    for i in range(len(seq)):
        if seq[i:i+targetLen] == target:
            return i
    return -1

def checkForPattern(history, window):
    history = history[::-1]
    print(history)

    target = history[:window]
    i = findTarget(history[window:], target)
    print(i)

    cycle = i + window
    if cycle > window:
        if history[:cycle] == history[cycle:cycle+cycle]:
            pattern = history[:cycle][::-1]
            length = len(pattern)
            history = history[::-1]
            start = findTarget(history, pattern)
            print(f"found pattern! {pattern} of length {length} starting at {start}")
            index = (1000000000-start-1) % length
            return history[start+index]
    return 0

data = open('data', 'r').read()
grid = makeGrid(data)

history = []
for i in range(1000000000):
    spinCycle(grid)
    load = calcLoad(grid)
    history.append(load)
    print(i, load)
    if i % 100 == 0:
        print(i)
        answer = checkForPattern(history, 20)
        if (answer):
            print(answer)
            break
