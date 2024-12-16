# https://adventofcode.com/2024/day/16

import numpy as np
import heapq
from collections import defaultdict

test1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

test2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
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

def solve(grid, start, end, direction):
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
    pq = [(0, start, direction)]
    came_from = {}

    while pq:
        cost, (r, c), d = heapq.heappop(pq)
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

        for ndir, mv in directions.items():
            nr, nc = r+mv[0], c+mv[1]
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr,nc] != '#':
                new_cost = cost + 1
                if d != ndir:
                    new_cost += 1000
                if new_cost < dist[(nr,nc)]:
                    dist[(nr,nc)] = new_cost
                    came_from[(nr,nc)] = (r, c)
                    heapq.heappush(pq, (new_cost, (nr,nc), ndir))

    return None, float('inf')  # No path found

def solve2(grid, start, end, direction):
    rows, cols = grid.shape
    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1),
    }

    dist = defaultdict(lambda: float('inf'))
    came_from = defaultdict(list)

    dist[(start[0], start[1], direction)] = 0
    pq = [(0, (start), direction)]

    while pq:
        cost, (r, c), d = heapq.heappop(pq)
        if cost > dist[(r,c,d)]:
            continue

        if (r, c) == end:
            # We do not break here because we want to ensure
            # we've found all minimal states for the end node.
            continue

        for ndir, (dr, dc) in directions.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] != '#':
                new_cost = cost + 1
                if d != ndir:
                    new_cost += 1000

                if new_cost < dist[(nr, nc, ndir)]:
                    dist[(nr, nc, ndir)] = new_cost
                    came_from[(nr, nc, ndir)] = [(r, c, d)]
                    heapq.heappush(pq, (new_cost, (nr, nc), ndir))
                elif new_cost == dist[(nr, nc, ndir)]:
                    # Another minimal-cost predecessor
                    came_from[(nr, nc, ndir)].append((r, c, d))

    # Find minimal states at the end cell
    min_cost = float('inf')
    end_states = []
    for direction_key in ['N', 'S', 'E', 'W']:
        if dist[(end[0], end[1], direction_key)] < min_cost:
            min_cost = dist[(end[0], end[1], direction_key)]
            end_states = [(end[0], end[1], direction_key)]
        elif dist[(end[0], end[1], direction_key)] == min_cost:
            end_states.append((end[0], end[1], direction_key))

    # If no path found
    if min_cost == float('inf'):
        return [], float('inf')

    # Backtrack to find all paths
    def backtrack(state):
        r, c, d = state
        if (r, c) == start:
            return [[(r, c)]]

        paths = []
        for (pr, pc, pd) in came_from[state]:
            for p in backtrack((pr, pc, pd)):
                paths.append(p + [(r, c)])
        return paths

    all_paths = []
    for st in end_states:
        for p in backtrack(st):
            all_paths.append(p)

    return all_paths, min_cost

input = test2
input = open('data', 'r').read()

grid = makeGrid(input)
#printGrid(grid)

ys, xs = np.where(grid == 'S')
start = list(zip(ys, xs))[0]

ys, xs = np.where(grid == 'E')
end = list(zip(ys, xs))[0]

#print(start, end)
paths, cost = solve2(grid, start, end, 'E')
#print(path)

for path in paths:
    for r, c in path:
        grid[r, c] = 'O';
printGrid(grid)

print(np.count_nonzero(grid == 'O'))
