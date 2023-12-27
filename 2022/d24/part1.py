import heapq
from collections import defaultdict
import numpy as np

data = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

# data = """#.#####
# #.....#
# #>....#
# #.....#
# #...v.#
# #.....#
# #####.#"""

class Map:
    def __init__(self, lines):
        blizzards = []

        self.h = len(lines)-2
        self.w = len(lines[0])-2

        for y in range(1, self.h+1):
            line = lines[y]
            for x in range(1, self.w+1):
                t = line[x]
                if t != '.':
                    blizzards.append((t, x, y))
        self.blizzards = blizzards

    def evolve(self):
        dxdy = { '>': (1,0), '<': (-1,0),'v': (0,1),'^': (0,-1) }
        next = []
        for t, x, y in self.blizzards:
            dx, dy = dxdy[t]
            x += dx
            y += dy

            if x < 1:
                x = self.w
            if x > self.w:
                x = 1
            if y < 1:
                y = self.h
            if y > self.h:
                y = 1

            next.append((t, x, y))
        self.blizzards = next

    def print(self, row, col):
        grid = np.full((self.h+2, self.w+2), '#')
        grid[1:-1,1:-1] = '.'
        for t, x, y in self.blizzards:
            if grid[y, x] == '.':
                grid[y, x] = t
            else:
                grid[y, x] = '*'
        grid[0,1] = '.'
        grid[-1,-2] = '.'
        grid[row, col] = 'E'

        print()
        for i in range(self.h+2):
            print("".join(grid[i,]))
        print()

def solve(map):
    costs = defaultdict(int)

    start = (0, 1)
    end = (map.h+1, map.w)
    rows = map.h+1
    cols = map.w+1
    row, col = start
    pqueue = [(0, row, col)]
    heapq.heapify(pqueue)
    visited = set()
    init = list(map.blizzards)
    cache = {}

    while len(pqueue) > 0:
        cost, row, col = heapq.heappop(pqueue)
        if (row, col, cost) in visited:
            continue
        visited.add((row, col, cost))
        costs[(row, col)] = cost

        if (row, col) == end:
            break

        step = cost+1
        if step not in cache:
            map.blizzards = init
            for _ in range(cost+1):
                map.evolve()
            cache[step] = map.blizzards
        else:
            map.blizzards = cache[step]

        blocked = [(y, x) for t, x, y in map.blizzards]

        for mv_y, mv_x in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            new_row = row + mv_y
            new_col = col + mv_x

            if not (0 < new_row < rows and 0 < new_col < cols) and (new_row, new_col) != end:
                continue

            if (new_row, new_col) in blocked:
                continue
            
            print('pushing', cost+1, new_row, new_col)
            heapq.heappush(pqueue, (cost+1, new_row, new_col))
    print(costs)            
    return costs[end]

data = open('data', 'r').read()
lines = data.split('\n')
map = Map(lines)
print('steps =', solve(map))
