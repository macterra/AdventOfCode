# https://adventofcode.com/2023/day/23

import numpy as np
from collections import defaultdict, deque

data = r"""
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""

# data = r"""
# .....
# ...#.
# ...#.
# ...#.
# ...#.
# ...#.
#"""

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

def getNeighbors(node, grid):
    row, col = node
    height, width = grid.shape
    neighbors = []

    if grid[row, col] == '.':
        if row > 0 and grid[row-1,col] != '#':
            neighbors.append((row-1, col))
        if col > 0 and grid[row,col-1] != '#':
            neighbors.append((row, col-1))
        if row < height-1 and grid[row+1,col] != '#':
            neighbors.append((row+1, col))
        if col < width-1 and grid[row,col+1] != '#':
            neighbors.append((row, col+1))
    elif grid[row, col] == '>':
        neighbors.append((row, col+1))
    elif grid[row, col] == '<':
        neighbors.append((row, col-1))
    elif grid[row, col] == '^':
        neighbors.append((row-1, col))
    elif grid[row, col] == 'v':
        neighbors.append((row+1, col))
    return neighbors

def longestPath(grid, start):
    stack = [(start, [start])]
    longest_path_length = 0
    longest_path = []
    while stack:
        node, path = stack.pop()
        for neighbor in getNeighbors(node, grid):
            if neighbor not in path:
                if len(path + [neighbor]) > longest_path_length:
                    longest_path_length = len(path + [neighbor])
                    longest_path = path + [neighbor]
                stack.append((neighbor, path + [neighbor]))
    return longest_path

maze = makeGrid(data)
printGrid(maze)

path = longestPath(maze, (0,1))

def printPath(grid, path):
    h, w = maze.shape
    dist = np.full((h, w), -1)
    for i in range(len(path)):
        row, col = path[i]
        dist[row, col] = i
    for row in dist:
        print("".join([f"{i:3}" for i in row]))

#printPath(maze, path)
print(len(path)-1)
