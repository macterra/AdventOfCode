# https://adventofcode.com/2023/day/8

import re

input = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

input = open('data', 'r').read()
lines = input.strip().split('\n')

print(lines)

def parse(lines):
    nodes = {}

    pattern = r"(\w+) = \((\w+), (\w+)\)"

    for line in lines:
        match = re.match(pattern, line)
        if match:
            a, b, c = match.groups()
            nodes[a] = (b, c)

    return nodes

path = lines[0]
nodes = parse(lines[2:])

print(path)
print(nodes)

i = 0
steps = 0
node = 'AAA'

while node != 'ZZZ':
    direction = path[i]
    steps += 1
    i = (i+1) % len(path)
    node = nodes[node][0] if direction == 'L' else nodes[node][1]
    print(steps, i, direction, node)
