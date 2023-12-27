# https://adventofcode.com/2023/day/3

import numpy as np

input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

input = open('data', 'r').read()

def makeGrid(input):
    lines = input.split('\n')[:-1]
    w = len(lines[0])
    h = len(lines)
    print(lines, w, h)
    grid = np.full((h+2,w+2), '.')
    for i in range(h):
        for j in range(w):
            grid[i+1,j+1] = lines[i][j]
    return grid

grid = makeGrid(input)
print(grid)

h, w = grid.shape
nums = {}

for i in range(0,h):
    num = ''
    for j in range(0,w):
        print(i, j, grid[i,j], grid[i,j].isdigit())
        if grid[i,j].isdigit():
            if not len(num):
                print(f"found a new number at {i},{j}")
                x, y = i, j
            num += grid[i,j]
            grid[i,j] = '.'
        else:
            if len(num):
                print(num)
                nums[(x,y,j-1)] = int(num)
            num = ''

print(nums)

sum = 0
for i, j, k in nums:
    print(i, j, k, nums[(i, j, k)])
    region = grid[i-1:i+2,j-1:k+2]
    print(region)
    if not (region == '.').all():
        sum += nums[(i, j, k)]

print(sum)
