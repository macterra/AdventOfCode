import numpy as np

input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

input = """8258741254
3335286211
8468661311
6164578353
2138414553
1785385447
3441133751
3586862837
7568272878
6833643144"""

def makeGrid(input):
    lines = input.split('\n')
    w = len(lines[0])
    h = len(lines)

    print(lines, w, h)

    grid = np.full((w+2,h+2), 99)

    for i in range(h):
        for j in range(w):
            grid[i+1, j+1] = int(lines[i][j])

    return grid

def step(grid, i, j):
    grid[(i,j)] += 1
    if grid[(i,j)] == 10:
        step(grid, i-1, j-1)
        step(grid, i-1, j)
        step(grid, i-1, j+1)
        step(grid, i, j-1)
        step(grid, i, j+1)
        step(grid, i+1, j-1)
        step(grid, i+1, j)
        step(grid, i+1, j+1)

grid = makeGrid(input)
w, h = grid.shape
flashes = 0

for x in range(100):
    print('step', x)
    print(grid)


    for i in range(1,h-1):
        for j in range(1,w-1):
            step(grid, i, j)

    for i in range(1,h-1):
        for j in range(1,w-1):
            if grid[(i,j)] > 9:
                flashes += 1
                grid[i,j] = 0

    print('flashes', flashes)
