# https://adventofcode.com/2025/day/6

lines = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""

lines = open('data', 'r').read()

input = lines.strip().split('\n')
grid = []
for line in input:
    row = []
    for cell in line.strip().split():
        row.append(cell)
    grid.append(row)


rows = len(grid)
cols = len(grid[0])

print("Grid size:", rows, "x", cols)
print(grid)

sum = 0
for col in range(cols):
    op = grid[rows - 1][col]
    print(f"Processing column {col} with operation '{op}'")
    total = 1 if op == '*' else 0
    for row in range(rows-1):
        val = int(grid[row][col])
        if op == '*':
            total *= val
        elif op == '+':
            total += val
    print(f"Column {col} result: {total}")
    sum += total

print("Final sum of column results:", sum)
