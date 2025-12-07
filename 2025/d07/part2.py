# https://adventofcode.com/2025/day/7

from functools import lru_cache

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

# import input into list of lists
input = lines.strip().split('\n')
max_len = max(len(line) for line in input)
grid = []
for line in input:
    row = list(line)
    # Pad the row to max_len with spaces if needed
    while len(row) < max_len:
        row.append(' ')
    grid.append(row)

rows = len(grid)
cols = len(grid[0])
print("Grid size:", rows, "x", cols)

# Convert grid to tuple for hashability (required for lru_cache)
grid_tuple = tuple(tuple(row) for row in grid)

@lru_cache(maxsize=None)
def timelineCounter(r, c):
    # if we hit bottom row, return 1
    if r == rows - 1:
        return 1

    if grid_tuple[r][c] == '.':
        return timelineCounter(r + 1, c)

    if grid_tuple[r][c] == '^':
        return timelineCounter(r + 1, c - 1) + timelineCounter(r + 1, c + 1)

# find S position
start_r, start_c = 0, None

for c in range(cols):
    if grid[start_r][c] == 'S':
        start_c = c
        break
grid[start_r][start_c] = '.'

grid_tuple = tuple(tuple(row) for row in grid)
timelines = timelineCounter(start_r, start_c)
print(timelines)
