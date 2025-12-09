# https://adventofcode.com/2025/day/9

lines = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

lines = open('data', 'r').read()

# import input into list of tuples
input = []
for line in lines.strip().split('\n'):
    parts = line.split(',')
    input.append((int(parts[0]), int(parts[1])))

print(input)

# for each pair of points, calcuate area of rectangle they form
max_area = 0
for i in range(len(input)):
    x1, y1 = input[i]
    for j in range(i + 1, len(input)):
        x2, y2 = input[j]
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height
        if area > max_area:
            max_area = area

print(max_area)
