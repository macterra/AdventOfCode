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

height, width = grid.shape

def addBeam(beams, d, row, col):
    global width
    global height

    if col < 0 or col >= width:
        return

    if row < 0 or row >= height:
        return

    beams.append((d, row, col))

def energized(beam):
    print(beam)
    beams = [beam]
    tracks = set()

    while beams:
        beam = beams.pop()

        if beam in tracks:
            continue
        tracks.add(beam)

        d, row, col = beam
        cell = grid[row, col]

        if cell == '.':
            if d == 'E':
                addBeam(beams, 'E', row, col+1)
            if d == 'W':
                addBeam(beams, 'W', row, col-1)
            if d == 'N':
                addBeam(beams, 'N', row-1, col)
            if d == 'S':
                addBeam(beams, 'S', row+1, col)

        if cell == '/':
            if d == 'E':
                addBeam(beams, 'N', row-1, col)
            if d == 'W':
                addBeam(beams, 'S', row+1, col)
            if d == 'N':
                addBeam(beams, 'E', row, col+1)
            if d == 'S':
                addBeam(beams, 'W', row, col-1)

        if cell == '\\':
            if d == 'E':
                addBeam(beams, 'S', row+1, col)
            if d == 'W':
                addBeam(beams, 'N', row-1, col)
            if d == 'N':
                addBeam(beams, 'W', row, col-1)
            if d == 'S':
                addBeam(beams, 'E', row, col+1)

        if cell == '|':
            if d == 'E':
                addBeam(beams, 'N', row-1, col)
                addBeam(beams, 'S', row+1, col)
            if d == 'W':
                addBeam(beams, 'N', row-1, col)
                addBeam(beams, 'S', row+1, col)
            if d == 'N':
                addBeam(beams, 'N', row-1, col)
            if d == 'S':
                addBeam(beams, 'S', row+1, col)

        if cell == '-':
            if d == 'E':
                addBeam(beams, 'E', row, col+1)
            if d == 'W':
                addBeam(beams, 'W', row, col-1)
            if d == 'N':
                addBeam(beams, 'E', row, col+1)
                addBeam(beams, 'W', row, col-1)
            if d == 'S':
                addBeam(beams, 'E', row, col+1)
                addBeam(beams, 'W', row, col-1)

    energized = set()
    for track in tracks:
        _, row, col = track
        energized.add((row, col))
    return len(energized)

emax = 0

for row in range(height):
    e = energized(('E', row, 0))
    print(e)
    emax = max(e, emax)
    e = energized(('W', row, width-1))
    print(e)
    emax = max(e, emax)

for col in range(width):
    e = energized(('S', 0, col))
    print(e)
    emax = max(e, emax)
    e = energized(('N', height-1, col))
    print(e)
    emax = max(e, emax)

print(emax)
