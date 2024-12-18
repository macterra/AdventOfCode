# https://adventofcode.com/2024/day/18

import numpy as np
import heapq
from collections import defaultdict

input = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

def makeGrid(input, sz, mx):
    lines = [line for line in input.split('\n') if line.strip() != '']
    grid = np.full((sz, sz), '.')
    for line in lines[:mx]:
        x, y = line.split(',')
        grid[int(y),int(x)] = '#'
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

def solve(grid, start, end):
    rows, cols = grid.shape

    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1),
    }

    visited = set()
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    came_from = {}

    while pq:
        cost, (r, c) = heapq.heappop(pq)
        if (r, c) == end:
            # We reached the end, can reconstruct the path here
            path = []
            current = end
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, dist[end]

        if (r, c) in visited:
            continue
        visited.add((r, c))

        for _, mv in directions.items():
            nr, nc = r+mv[0], c+mv[1]
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr,nc] != '#':
                new_cost = cost + 1
                if new_cost < dist[(nr,nc)]:
                    dist[(nr,nc)] = new_cost
                    came_from[(nr,nc)] = (r, c)
                    heapq.heappush(pq, (new_cost, (nr,nc)))

    return None, float('inf')  # No path found

input = open('data', 'r').read()
grid = makeGrid(input, 71, 1024)
printGrid(grid)
path, dist = solve(grid, (0,0), (70,70))
print(path, dist)

for r, c in path:
    grid[r, c] = 'O'
printGrid(grid)
print(dist)
