# https://adventofcode.com/2025/day/6

import numpy as np

lines = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""

lines = open('data', 'r').read()

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

rows = len(grid)
cols = len(grid[0])

print("Grid size:", rows, "x", cols)
print(grid)

# copy grid into a numpy array for easier manipulation
np_grid = np.array(grid)
print("Numpy Grid:")
print(np_grid)

# pivot grid along diagonal
pivoted_grid = np_grid.T
print("Pivoted Grid:")
print(pivoted_grid)

# get rows and cols of pivoted grid
rows, cols = pivoted_grid.shape
print("Pivoted Grid size:", rows, "x", cols)

sum = 0
row = 0
op = ''

while row < rows:
    if not op:
        op = pivoted_grid[row, cols-1]
        print(f"Processing row {row} with operation '{op}'")
        total = 1 if op == '*' else 0
    # get slice of each row excluding last column
    num = "".join(pivoted_grid[row, :cols-1]).strip()
    if len(num) > 0:
        val = int(num)
        print(f"  Value: {val}")
        if op == '*':
            total *= val
        elif op == '+':
            total += val
    else:
        sum += total
        op = ''
    row += 1

print("Final sum of column results:", sum+total)
