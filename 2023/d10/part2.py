# https://adventofcode.com/2023/day/10

import numpy as np

data = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

data = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

data = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

data = open('data', 'r').read()

def makeGrid(input):
    lines = input.strip().split('\n')
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h,w), '.')
    for i in range(h):
        for j in range(w):
            grid[i,j] = lines[i][j]
    return grid

grid = makeGrid(data)

h, w = grid.shape
bigGrid = np.full((h*3, w*3), '.')

loc = np.where(grid == 'S')
row, col = loc[0][0], loc[1][0]
print(row, col)

moves = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

pipes = {
    '|': { 'N': 'N', 'S': 'S' },
    '-': { 'E': 'E', 'W': 'W' },
    'L': { 'S': 'E', 'W': 'N' },
    'J': { 'S': 'W', 'E': 'N' },
    '7': { 'E': 'S', 'N': 'W' },
    'F': { 'W': 'S', 'N': 'E' },
}

tile1 = """
.x.
.x.
.x.
"""

tile2 = """
...
xxx
...
"""

tile3 = """
.x.
.xx
...
"""

tile4 = """
.x.
xx.
...
"""

tile5 = """
...
xx.
.x.
"""

tile6 = """
...
.xx
.x.
"""

tiles = {
    '|': makeGrid(tile1),
    '-': makeGrid(tile2),
    'L': makeGrid(tile3),
    'J': makeGrid(tile4),
    '7': makeGrid(tile5),
    'F': makeGrid(tile6),
}

# hard-coded hint
direction = 'E'
bigGrid[row*3:row*3+3, col*3:col*3+3] = tiles['-']

steps = 0
while True:
    dr, dc = moves[direction]
    row += dr
    col += dc
    cell = grid[row,col]
    if cell == 'S':
        break
    bigGrid[row*3:row*3+3, col*3:col*3+3] = tiles[cell]
    direction = pipes[cell][direction]
    steps += 1

print(steps)
print((steps+1)//2)

def printGrid(grid):
    for row in grid:
        print("".join(list(row)))

printGrid(bigGrid)

def floodFill(grid):
    queue = [(0, 0)]
    visited = set()
    rows, cols = grid.shape

    while queue:
        loc = queue.pop(0)

        if loc not in visited:
            visited.add(loc)
            row, col = loc
            if grid[row, col] == '.':
                grid[row, col] = 'o'

                if row > 0:
                    queue.append((row-1, col))
                if row < (rows-1):
                    queue.append((row+1, col))
                if col > 0:
                    queue.append((row, col-1))
                if col < (cols-1):
                    queue.append((row, col+1))

floodFill(bigGrid)
printGrid(bigGrid)

inside = 0
for row in range(0, h):
    for col in range(0, w):
        cell = bigGrid[row*3:row*3+3, col*3:col*3+3]
        if np.all(cell == '.'):
            inside += 1
print(inside)
