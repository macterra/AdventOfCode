# https://adventofcode.com/2023/day/21

import numpy as np
import heapq

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

def shortestPath(start, end, graph_func):
    queue = [(0, start)]
    heapq.heapify(queue)
    visited = set()
    while queue:
        (dist, current) = heapq.heappop(queue)

        if dist > 64:
            return -1

        if current in visited:
            continue
        visited.add(current)

        if current == end:
            return dist

        for next_node, distance in graph_func(current):
            heapq.heappush(queue, (dist + distance, next_node))
    return -1

garden = makeGrid(data)
printGrid(garden)

def adjacentNodes(loc):
    global garden

    adjacent = []
    h, w = garden.shape
    row, col = loc

    if row > 0 and garden[row-1, col] != '#':
        adjacent.append(((row-1, col), 1))

    if col > 0 and garden[row, col-1] != '#':
        adjacent.append(((row, col-1), 1))

    if row < h-1 and garden[row+1, col]!= '#':
        adjacent.append(((row+1, col), 1))

    if col< w-1 and garden[row, col+1] != '#':
        adjacent.append(((row, col+1), 1))

    return adjacent

sloc = np.where(garden == 'S')
start = (sloc[0][0], sloc[1][0])
print(start)

height, width = garden.shape
grid = np.full((height, width), -1)

for row in range(height):
    for col in range(width):
        if garden[row, col] != '#':
            grid[row, col] = shortestPath((row,col), start, adjacentNodes)

print(grid)
print(np.count_nonzero(grid%2 == 0))
