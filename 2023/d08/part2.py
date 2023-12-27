import re
import math
# https://adventofcode.com/2023/day/8

input = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX
"""

input = open('data', 'r').read()
lines = input.strip().split('\n')

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

ghosts = [ node for node in nodes if node[2] == 'A' ]
print(ghosts)

def findCycle(ghost, path):
    node = ghost
    i = 0
    steps = 0

    while True:
        direction = path[i]
        steps += 1
        i = (i+1) % len(path)
        node = nodes[node][0] if direction == 'L' else nodes[node][1]
        if node[2] == 'Z':
            return steps

cycles = [findCycle(ghost, path) for ghost in ghosts]
print(cycles)

def lcm(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result = abs(result*i) // math.gcd(result, i)
    return result

print(lcm(cycles))
