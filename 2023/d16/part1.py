# https://adventofcode.com/2023/day/16

import numpy as np

data = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

data = open('data', 'r').read()

def makeGrid(input):
    lines = input.strip().split('\n')
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h,w), 'x')
    for i in range(h):
        for j in range(w):
            grid[i,j] = lines[i][j]
    return grid

def printGrid(grid):
    for row in grid:
        print("".join(list(row)))

grid = makeGrid(data)
printGrid(grid)

beam = ('E', 0, 0)
beams = [beam]
tracks = set()

height, width = grid.shape

def addBeam(d, row, col):
    global beams
    global width
    global height

    if col < 0 or col >= width:
        return

    if row < 0 or row >= height:
        return

    beams.append((d, row, col))

while beams:
    print(beams)
    beam = beams.pop()

    if beam in tracks:
        continue
    tracks.add(beam)

    d, row, col = beam
    cell = grid[row, col]

    print(d, row, col, cell)

    if cell == '.':
        if d == 'E':
            addBeam('E', row, col+1)
        if d == 'W':
            addBeam('W', row, col-1)
        if d == 'N':
            addBeam('N', row-1, col)
        if d == 'S':
            addBeam('S', row+1, col)

    if cell == '/':
        if d == 'E':
            addBeam('N', row-1, col)
        if d == 'W':
            addBeam('S', row+1, col)
        if d == 'N':
            addBeam('E', row, col+1)
        if d == 'S':
            addBeam('W', row, col-1)

    if cell == '\\':
        if d == 'E':
            addBeam('S', row+1, col)
        if d == 'W':
            addBeam('N', row-1, col)
        if d == 'N':
            addBeam('W', row, col-1)
        if d == 'S':
            addBeam('E', row, col+1)

    if cell == '|':
        if d == 'E':
            addBeam('N', row-1, col)
            addBeam('S', row+1, col)
        if d == 'W':
            addBeam('N', row-1, col)
            addBeam('S', row+1, col)
        if d == 'N':
            addBeam('N', row-1, col)
        if d == 'S':
            addBeam('S', row+1, col)

    if cell == '-':
        if d == 'E':
            addBeam('E', row, col+1)
        if d == 'W':
            addBeam('W', row, col-1)
        if d == 'N':
            addBeam('E', row, col+1)
            addBeam('W', row, col-1)
        if d == 'S':
            addBeam('E', row, col+1)
            addBeam('W', row, col-1)

energized = set()
for track in tracks:
    _, row, col = track
    energized.add((row, col))

print(len(energized))
