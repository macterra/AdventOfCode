import numpy as np

input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

input = open('data', 'r').read()

def makeGrid(input):
    lines = input.split('\n')
    w = len(lines[0])
    h = len(lines)
    print(lines, w, h)
    grid = np.full((h+2,w+2), 99)
    for i in range(h):
        for j in range(w):
            grid[i+1,j+1] = int(lines[i][j])
    return grid

def isLow(grid, x, y):
    v = grid[x,y]
    return v < grid[x-1,y] and v < grid[x+1,y] and v < grid[x,y-1] and v < grid[x,y+1]

grid = makeGrid(input)
print(grid)
h, w = grid.shape
print(h, w)
risk = 0
for i in range(1,h-1):
    for j in range(1,w-1):
        if isLow(grid, i, j):
            print(i, j, grid[i,j])
            risk += 1 + grid[i,j]
print(risk)
