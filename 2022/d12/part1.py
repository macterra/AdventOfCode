import numpy as np
import heapq
from collections import defaultdict

data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

def makeGrid(lines):
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h,w), 0)
    for i in range(h):
        for j in range(w):
            c = lines[i][j]
            if c == 'S':
                c = 'a'
                start = (i,j)
            elif c == 'E':
                c = 'z'
                end = (i,j)                
            grid[i,j] = ord(c) - ord('a')
    return grid, start, end

def solve(grid, start, end):
    rows, cols = grid.shape
    costs = defaultdict(int)

    x, y = start
    pqueue = [(0, x, y)]
    heapq.heapify(pqueue)
    visited = set()
    while len(pqueue) > 0:
        cost, row, col = heapq.heappop(pqueue)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        costs[(row, col)] = cost

        if (row, col) == end:
            break

        for mv_y, mv_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + mv_y
            new_col = col + mv_x

            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            if grid[new_row,new_col] - grid[row,col] > 1:
                continue
            
            heapq.heappush(pqueue, (cost+1, new_row, new_col))
    #print(costs)            
    return costs[end]

data = open('data', 'r').read()
lines = data.split('\n')
grid, start, end = makeGrid(lines)
print(grid)
print(start, end)
cost = solve(grid, start, end)
print(cost)