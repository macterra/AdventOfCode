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

path, dist = solve(grid, start, end)
#print(path)
print(dist)

times = {}
for t, coord in enumerate(path):
    print(t, coord)
    times[coord] = dist - t
print(times)

max_cheat = 20
counts = defaultdict(int)
saved = {}
h, w = grid.shape

for t, coord in enumerate(path):
    i, j = coord
    for r in range(i - max_cheat, i + max_cheat + 1):
        for c in range(j - max_cheat, j + max_cheat + 1):
            time_used = abs(r - i) + abs(c - j)
            if not (0 <= r < h and 0 <= c < w) or time_used > max_cheat or grid[r, c] == "#":
                continue

            rem_t = times[(r, c)]
            saved[(i, j, r, c)] = dist - (t + rem_t + time_used)

for v in saved.values():
    if v >= 100:
        counts[v] += 1

for k, v in counts.items():
    print(k, v)

print(sum(counts.values()))
