# https://adventofcode.com/2023/day/11

import numpy as np

data = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
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

def expandSpace(grid):
    h, w = grid.shape
    for row in range(h):
        if not np.any(grid[row] == '#'):
            grid[row] = np.full(w, 'x')

    for col in range(w):
        if not np.any(grid[:,col] == '#'):
            grid[:,col] = np.full(h, 'x')

    return grid

grid = makeGrid(data)
grid = expandSpace(grid)

# printGrid(grid)

loc = np.where(grid == '#')
galaxies = list(zip(*loc))

#print(galaxies)

def shortestPath(galaxy, galaxies, grid):
    dist = 0
    r1, c1 = galaxy
    for r2, c2 in galaxies:
        foo = grid[r1, min(c1,c2):max(c1,c2)]
        bar = grid[min(r1,r2):max(r1,r2), c1]

        dist += np.count_nonzero(foo != 'x')
        dist += np.count_nonzero(foo == 'x') * 1000000
        dist += np.count_nonzero(bar != 'x')
        dist += np.count_nonzero(bar == 'x') * 1000000
    return dist

sum = 0
for i in range(0, len(galaxies)-1):
    sum += shortestPath(galaxies[i], galaxies[i+1:], grid)

print(sum)
