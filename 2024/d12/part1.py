# https://adventofcode.com/2024/day/12

import numpy as np

input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

input = open('data', 'r').read()

def makeGrid(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h+2,w+2), '.')
    for i in range(h):
        for j in range(w):
            grid[i+1,j+1] = lines[i][j]
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

grid = makeGrid(input)
printGrid(grid)

visited = []
regions = {}
h, w = grid.shape

def flood(i, j):
    loc = (i, j)
    if loc in visited:
        return []
    visited.append(loc)

    plant = grid[i, j]
    region = [loc]

    if grid[i-1, j] == plant:
        region += flood(i-1, j)
    if grid[i+1, j] == plant:
        region += flood(i+1, j)
    if grid[i, j-1] == plant:
        region += flood(i, j-1)
    if grid[i, j+1] == plant:
        region += flood(i, j+1)

    return region

regions = []
for i in range(1, h-1):
    for j in range(1, w-1):
        region = flood(i, j)
        if len(region) > 0:
            regions.append(region)

total = 0
for region in regions:
    i, j = region[0]
    plant = grid[i, j]
    area = len(region)
    perimeter = 0
    for i, j in region:
        if grid[i-1, j] != plant:
            perimeter += 1
        if grid[i+1, j] != plant:
            perimeter += 1
        if grid[i, j-1] != plant:
            perimeter += 1
        if grid[i, j+1] != plant:
            perimeter += 1
    print(plant, area, perimeter, area * perimeter)
    total += area * perimeter
print(total)
