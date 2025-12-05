# https://adventofcode.com/2025/day/5

lines = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

lines = open('data', 'r').read()

ranges, ingredients = lines.strip().split('\n\n')

ranges = ranges.split('\n')
ranges = [tuple(map(int, r.split('-'))) for r in ranges]
ranges.sort()

print("Ranges:", ranges, len(ranges))

# merge overlapping ranges
merged_ranges = []
for r in ranges:
    if not merged_ranges or merged_ranges[-1][1] < r[0]:
        merged_ranges.append(r)
    else:
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], r[1]))

print("Ranges:", merged_ranges, len(merged_ranges))

fresh = 0
for a, b in merged_ranges:
    fresh += (b - a + 1)

print("Fresh ingredients count:", fresh)
