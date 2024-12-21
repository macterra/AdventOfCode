# https://adventofcode.com/2024/day/20

import numpy as np
import heapq
from collections import defaultdict

input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

def makeGrid(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h,w), '.')
    for i in range(h):
        for j in range(w):
            grid[i, j] = lines[i][j]
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

grid = makeGrid(input)
printGrid(grid)

ys, xs = np.where(grid == 'S')
start = list(zip(ys, xs))[0]

ys, xs = np.where(grid == 'E')
end = list(zip(ys, xs))[0]

print(start, end)

_, baseTime = solve(grid, start, end)
print(baseTime)

def inPath(path, cheat):
    try:
        i = path.index(cheat[0])
        return path[i+1] == cheat[1]
    except ValueError:
        return False

savedTimes = {}

def checkCheat(cheat):
    grid2 = grid.copy()
    grid2[cheat[0]] = '.'
    path, cheatTime = solve(grid2, start, end)
    if cheatTime < baseTime and inPath(path, cheat):
        saved = baseTime - cheatTime
        if saved >= 100:
            print(cheat, saved)
            savedTimes[saved] = savedTimes.get(saved, 0) + 1

h, w = grid.shape

for r in range(1, h-1):
    for c in range(1, w-1):
        if grid[r, c] == '#':
            if c < (w-1):
                checkCheat([(r, c), (r, c+1)])
            if c > 1:
                checkCheat([(r, c), (r, c-1)])
            if r < (h-1):
                checkCheat([(r, c), (r+1, c)])
            if r > 1:
                checkCheat([(r, c), (r-1, c)])

for k in sorted(savedTimes.keys()):
    print(f"{k}: {savedTimes[k]}")
print(sum(savedTimes.values()))
