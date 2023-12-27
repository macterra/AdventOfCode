# https://adventofcode.com/2023/day/17

import numpy as np
import heapq

data = r"""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

# data = """
# 111111111111
# 999999999991
# 999999999991
# 999999999991
# 999999999991
# """

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
    queue = [(0, start, [], '?', [])]
    heapq.heapify(queue)
    visited = set()
    while queue:
        (dist, current, path, direction, directions) = heapq.heappop(queue)

        path = path + [current]
        directions = directions + [direction]

        loc = (current, "".join(directions[-10:]))
        if loc in visited:
            continue
        visited.add(loc)

        # print(dist, current, directions)

        if current == end:
            s, _ = streak(directions)
            if s < 4:
                continue
            return dist, path, directions

        for next_direction, next_node, distance in graph_func(current, directions):
            if next_node not in path:
                heapq.heappush(queue, (dist + distance, next_node, path, next_direction, directions))
    return -1, [], []

def streak(directions):
    if not directions:
        return 0, ''

    last = directions[-1]
    s = 0
    for d in directions[::-1]:
        if d == last:
            s += 1
        else:
            break
    return s, last

def getAdjacentNodes(node, directions):
    global grid
    global height
    global width

    directions = "".join(directions)[1:]
    s, last = streak(directions)
    allowed = '^v><'

    if s == 0:
        pass
    elif s < 4:
        allowed = last
    elif s > 9:
        allowed = allowed.replace(last, '')

    adjacent = []
    row, col = node

    if row > 0 and '^' in allowed:
        adjacent.append(('^', (row-1, col), int(grid[row-1,col])))

    if row < (height-1) and 'v' in allowed:
        adjacent.append(('v', (row+1, col), int(grid[row+1,col])))

    if col > 0 and '<' in allowed:
        adjacent.append(('<', (row, col-1), int(grid[row,col-1])))

    if col < (width-1) and '>' in allowed:
        adjacent.append(('>', (row, col+1), int(grid[row,col+1])))

    # print(node, s, last, allowed, directions, adjacent)

    return adjacent

grid = makeGrid(data)
printGrid(grid)

height, width = grid.shape
start = (0, 0)
end = (height-1, width-1)

loss, path, directions = shortestPath(start, end, getAdjacentNodes)
print(path)
print(directions)
printGrid(grid)

x = [int(grid[row, col]) for row, col in path]
print(x, sum(x))

for i in range(len(path)):
    grid[path[i]] = directions[i]

printGrid(grid)
print(loss)
