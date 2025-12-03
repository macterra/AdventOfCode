# https://adventofcode.com/2025/day/3

lines = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

f = open('data', 'r')
lines = f.read()

input = lines.strip().split('\n')

grid = []
for line in input:
    grid.append([int(c) for c in line])
#print(grid)

sum = 0
for row in range(len(grid)):
    bank = grid[row]
    # find max value in bank and its index excluding last digit
    max_val1 = -1
    max_idx1 = -1
    for i in range(len(bank) - 1):
        if bank[i] > max_val1:
            max_val1 = bank[i]
            max_idx1 = i
    print(bank)
    print(f"Row {row}: Max value {max_val1} at index {max_idx1}")

    # find max value after max_idx
    max_val2 = -1
    max_idx2 = -1
    for i in range(max_idx1 + 1, len(bank)):
        if bank[i] > max_val2:
            max_val2 = bank[i]
            max_idx2 = i
    print(f"Row {row}: Second max value {max_val2} at index {max_idx2}")
    sum += max_val1 * 10 + max_val2

print(f"Total sum: {sum}")
