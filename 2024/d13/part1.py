# https://adventofcode.com/2024/day/13

import re

input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

input = open('data', 'r').read()

def parseInput(input):
    blocks = input.split('\n\n')
    machines = []
    for block in blocks:
        lines = [line for line in block.split('\n') if line.strip() != '']
        match = re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])
        xa = int(match.group(1))
        ya = int(match.group(2))
        match = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])
        xb = int(match.group(1))
        yb = int(match.group(2))
        match = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[2])
        xp = int(match.group(1))
        yp = int(match.group(2))
        machines.append((xa, ya, xb, yb, xp, yp))
    return machines

def playMachine(machine):
    xa, ya, xb, yb, xp, yp = machine
    # solve for i and j
    # i * xa + j * xb = xp
    # i * ya + j * yb = yp

    # Determine the determinant of the coefficient matrix
    det = xa * yb - ya * xb

    # Solve for i and j using Cramer's rule
    i = (xp * yb - yp * xb) / det
    j = (-xp * ya + yp * xa) / det

    print(xa, ya, xb, yb, xp, yp, i, j)

    # Check if i and j are integers
    if i.is_integer() and j.is_integer():
        i, j = int(i), int(j)
        if i <= 100 and j <= 100:
            return i * 3 + j
    return 0

machines = parseInput(input)
total = 0
for machine in machines:
    total += playMachine(machine)
print(total)

