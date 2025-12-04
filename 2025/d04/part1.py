# https://adventofcode.com/2025/day/4

lines = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

f = open('data', 'r')
lines = f.read()

input = lines.strip().split('\n')
grid = []
for line in input:
    grid.append([c for c in line])
height = len(grid)
width = len(grid[0])

print(f"Grid size: {width}x{height}")
print(grid)

sum = 0
for r in range(height):
    for c in range(width):
        if grid[r][c] == '@':
            count = 0
            # check N
            if r > 0 and grid[r-1][c] == '@':
                count += 1
            # check S
            if r < height - 1 and grid[r+1][c] == '@':
                count += 1
            # check W
            if c > 0 and grid[r][c-1] == '@':
                count += 1
            # check E
            if c < width - 1 and grid[r][c+1] == '@':
                count += 1
            # check NW
            if r > 0 and c > 0 and grid[r-1][c-1] == '@':
                count += 1
            # check NE
            if r > 0 and c < width - 1 and grid[r-1][c+1] == '@':
                count += 1
            # check SW
            if r < height - 1 and c > 0 and grid[r+1][c-1] == '@':
                count += 1
            # check SE
            if r < height - 1 and c < width - 1 and grid[r+1][c+1] == '@':
                count += 1

            print(f"Cell ({r},{c}) has {count} adjacent '@' cells.")
            if count < 4:
                sum += 1

print(f"Sum: {sum}")
