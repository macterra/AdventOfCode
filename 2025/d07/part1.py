# https://adventofcode.com/2025/day/7

import numpy as np

lines = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

lines = open('data', 'r').read()

# import input into numpy array
input = lines.strip().split('\n')
max_len = max(len(line) for line in input)
grid = []
for line in input:
    row = []
    for cell in line:
        row.append(cell)
    # Pad the row to max_len with spaces if needed
    while len(row) < max_len:
        row.append(' ')
    grid.append(row)


grid = np.array(grid)
rows, cols = grid.shape
print("Grid size:", rows, "x", cols)
print(grid)

# find S position
start_pos = np.argwhere(grid == 'S')[0]
print("Start position:", start_pos)

# emit beam from S
grid[1, start_pos] = '|'

print(grid)
splits = 0
for r in range(rows):
    for c in range(cols):
        if r < rows - 1 and grid[r, c] == '|':
            # beam moves down
            if grid[r+1, c] == '.':
                grid[r+1, c] = '|'
            elif grid[r+1, c] == '^':
                splits += 1
                if c > 0:
                    grid[r+1, c-1] = '|'
                if c < cols - 1:
                    grid[r+1, c+1] = '|'

print(grid)
print(splits)
