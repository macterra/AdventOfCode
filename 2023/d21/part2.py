# https://adventofcode.com/2023/day/21

import numpy as np
from collections import deque

data = r"""
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
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

def printGrid(grid):
    for row in grid:
        print("".join(list(row)))

def calcReachable(grid, steps):
    height, width = grid.shape
    sloc = np.where(grid == 'S')
    start = (sloc[0][0], sloc[1][0])

    visited = set()
    queue = deque([start])
    reachable = []
    total = [0, 0]  # [even, odd]
    for step in range(1, steps+1):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if (i, j) in visited or grid[i%height, j%width] == '#':
                    continue

                visited.add((i, j))
                queue.append((i, j))
                total[step % 2] += 1
        reachable.append(list(total))
    return reachable

garden = makeGrid(data)
height, width = garden.shape

printGrid(garden)
reachable = calcReachable(garden, 328)

x_final, remainder = divmod(26_501_365, width)
crossings = [remainder, remainder + width, remainder + 2*width]

X = [0, 1, 2]
Y = [reachable[x][x%2] for x in crossings]

coefficients = np.polyfit(X, Y, deg=2)
y_final = np.polyval(coefficients, x_final)
print(y_final.round().astype(int))
