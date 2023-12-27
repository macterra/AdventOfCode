# https://adventofcode.com/2023/day/18

import numpy as np

data = r"""
R 26 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 22 (#015232)
U 2 (#7a21e3)
"""

data = open('data', 'r').read()

def parse(data):
    plan = []

    directions = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U',
    }

    for line in data.strip().split('\n'):
        d, n, color = line.split(' ')
        d = directions[color[-2]]
        n = int(color[2:7], base=16)
        #print(f"{color[2:7]} = {n}")
        plan.append((d, n))
    return plan

def dig(plan):
    trench = []
    row = 0
    col = 0
    for d, n in plan:
        if d == 'U':
            row -= n
        if d == 'D':
            row += n
        if d == 'L':
            col -= n
        if d == 'R':
            col += n
        trench.append((row, col))
    return trench

def shoelace_area(vertices):
    area = 0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) // 2
    return area

plan = parse(data)
trench = dig(plan)
area = shoelace_area(trench)
perim = sum([x for _, x in plan])
print(area, perim, area + perim//2 + 1)
