# https://adventofcode.com/2023/day/23

import numpy as np
from collections import deque

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

data = open('data', 'r').read()
grid = makeGrid(data)
#printGrid(grid)

def getNeighbors(node):
    global grid

    row, col = node
    height, width = grid.shape
    neighbors = []

    if grid[row, col] != '#':
        if row > 0 and grid[row-1,col] != '#':
            neighbors.append((row-1, col))
        if col > 0 and grid[row,col-1] != '#':
            neighbors.append((row, col-1))
        if row < height-1 and grid[row+1,col] != '#':
            neighbors.append((row+1, col))
        if col < width-1 and grid[row,col+1] != '#':
            neighbors.append((row, col+1))
    return neighbors

def shortestPath(start, end):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbor in getNeighbors(node):
            if neighbor not in path:
                if neighbor == end:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    return []

def printPath(grid, path):
    h, w = grid.shape
    dist = np.full((h, w), -1)
    for i in range(len(path)):
        row, col = path[i]
        dist[row, col] = i
    for row in dist:
        print("".join([f"{i:4}" for i in row]))

def makeGraph(grid):
    height, width = grid.shape
    graph = {}
    for row in range(height):
        for col in range(width):
            neighbors = getNeighbors((row, col))
            if neighbors:
                graph[(row, col)] = { n: 1 for n in neighbors}
    return graph

def reduceGraph(graph):
    # Make a copy of the graph to avoid modifying the original
    new_graph = {node: adj.copy() for node, adj in graph.items()}

    # Function to check if a node is linear (two neighbors)
    def is_linear(node):
        return len(new_graph[node]) == 2

    # Keep track of modified nodes to avoid double processing
    modified = set()

    # Process each node
    for node in list(new_graph.keys()):
        if node not in modified and is_linear(node):
            neighbors = list(new_graph[node].keys())

            # Merge the node with its neighbors if they aren't already directly connected
            if neighbors[0] not in new_graph[neighbors[1]]:
                new_weight = new_graph[node][neighbors[0]] + new_graph[node][neighbors[1]]

                # Create new direct connection
                new_graph[neighbors[0]][neighbors[1]] = new_weight
                new_graph[neighbors[1]][neighbors[0]] = new_weight

            # Remove the old node and its connections
            del new_graph[neighbors[0]][node]
            del new_graph[neighbors[1]][node]
            del new_graph[node]

            # Mark neighbors as modified
            modified.update(neighbors)

    return new_graph

def longestPath(graph, start, end):
    stack = [(start, [start], 0)]
    longest_path_length = 0
    longest_path = []
    while stack:
        node, path, dist = stack.pop()
        for neighbor, weight in graph[node].items():
            if neighbor not in path:
                if neighbor == end:
                    if dist+weight > longest_path_length:
                        longest_path_length = dist+weight
                        longest_path = path + [neighbor]
                else:
                    stack.append((neighbor, path + [neighbor], dist+weight))
    return longest_path, longest_path_length

graph = makeGraph(grid)
print(len(graph))

size = len(graph)
while True:
    graph = reduceGraph(graph)
    newsize = len(graph)
    if size == newsize:
        break
    size = newsize

h, w = grid.shape
print(longestPath(graph, (0,1), (h-1,w-2)))
