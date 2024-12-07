# https://adventofcode.com/2024/day/7

input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

input = open('data', 'r').read()

def parseEquations(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    equations = []
    for line in lines:
        res, vals = line.split(': ')
        vals = [int(x) for x in vals.split(' ')]
        equations.append((int(res), vals))
    return equations

def evalEquation(res, vals):
    print(res, vals)
    if len(vals) == 1:
        return res == vals[0]
    return evalEquation(res, [vals[0] + vals[1]] + vals[2:]) or evalEquation(res, [vals[0] * vals[1]] + vals[2:])

equations = parseEquations(input)
print(equations)
total = 0
for res, vals in equations:
    if evalEquation(res, vals):
        total += res

print(total)
