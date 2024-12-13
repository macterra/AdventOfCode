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

def calcSides(region):
    sides = []
    p = grid[region[0]]
    for i, j in region:
        if grid[i-1, j] != p:
            sides.append(('N', i, j, 1))
        if grid[i+1, j] != p:
            sides.append(('S', i, j, 1))
        if grid[i, j-1] != p:
            sides.append(('W', i, j, 1))
        if grid[i, j+1] != p:
            sides.append(('E', i, j, 1))
    #print(p, sides)
    while consolidate(sides):
        pass
    return len(sides)

def consolidate(sides):
    for i in range(len(sides)):
        for j in range(len(sides)):
            if i == j:
                continue
            d1, i1, j1, l1 = sides[i]
            d2, i2, j2, l2 = sides[j]

            if d1 == 'N' or d1 == 'S':
                if d2 == d1 and i1 == i2 and j1+l1 == j2:
                    if i > j:
                        sides.pop(i)
                        sides.pop(j)
                    else:
                        sides.pop(j)
                        sides.pop(i)

                    sides.append((d1, i1, j1, l1+l2))
                    return True

            if d1 == 'E' or d1 == 'W':
                if d2 == d1 and j1 == j2 and i1+l1 == i2:
                    if i > j:
                        sides.pop(i)
                        sides.pop(j)
                    else:
                        sides.pop(j)
                        sides.pop(i)

                    sides.append((d1, i1, j1, l1+l2))
                    return True
    return False

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
    sides = calcSides(region)
    print(plant, area, sides, area * sides)
    total += area * sides
print(total)
