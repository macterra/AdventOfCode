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

sum = 0
for row in range(len(grid)):
    bank = grid[row]
    joltage = []
    max_index = -1

    for i in range(12):
        max_digit = -1
        a = max_index + 1
        b = len(bank) + i - 11
        #print(i, a, b)
        for j in range(a, b):
            if bank[j] > max_digit:
                max_digit = bank[j]
                max_index = j
        joltage.append(max_digit)

    print(bank)
    print(joltage)
    total = int("".join(map(str, joltage)))
    print(total)
    sum += total

print(f"Total sum: {sum}")
