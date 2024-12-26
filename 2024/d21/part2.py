# https://adventofcode.com/2024/day/21

from sys import maxsize
from itertools import pairwise, permutations

input = """
029A
980A
179A
456A
379A
"""

input = open('data', 'r').read()

dir_base_lookup = {
    ('A', 'A'): 'A',
    ('^', '^'): 'A',
    ('>', '>'): 'A',
    ('v', 'v'): 'A',
    ('<', '<'): 'A',
    ('A', '^'): '<A',
    ('^', 'A'): '>A',
    ('A', '>'): 'vA',
    ('>', 'A'): '^A',
    ('v', '^'): '^A',
    ('^', 'v'): 'vA',
    ('v', '<'): '<A',
    ('<', 'v'): '>A',
    ('v', '>'): '>A',
    ('>', 'v'): '<A',

    ('A', 'v'): '<vA',
    ('v', 'A'): '^>A',
    ('A', '<'): 'v<<A',
    ('<', 'A'): '>>^A',

    ('>', '<'): '<<A',
    ('<', '>'): '>>A',
    ('<', '^'): '>^A',
    ('^', '<'): 'v<A',
    ('>', '^'): '<^A',
    ('^', '>'): 'v>A',
}

dirs = [
    [('^', -1), ('v', 1)],
    [('<', -1), ('>', 1)],
]

numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

numpad_lookup = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    ' ': (3, 0), '0': (3, 1), 'A': (3, 2),
}

dirpad = [
    [' ', '^', 'A'],
    ['<', 'v', '>'],
]

dirpad_lookup = {
    ' ': (0, 0), '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}

memo_dir = {}
def dir_solve(s, depth):
    if depth == 0:
        return len(s)
    if out := memo_dir.get((s, depth)):
        return out
    out = sum(
        dir_solve(dir_base_lookup[key_start, key_end], depth - 1)
        for key_start, key_end in pairwise(f"A{s}")
    )

    memo_dir[s, depth] = out
    return out

def num_solve(key_start, key_end):
    y0, x0 = numpad_lookup[key_start]
    y1, x1 = numpad_lookup[key_end]
    y_dist, x_dist = y1 - y0, x1 - x0
    y_key, y_dir = dirs[0][y_dist > 0]
    x_key, x_dir = dirs[1][x_dist > 0]

    # To dodge blank corner
    start_move = ""
    mov_s = ""
    if (y0 == 3 or y1 == 3) and (x0 == 0 or x1 == 0):
        if x0 == 0:
            start_move = '>'
            mov_s = y_key * abs(y_dist) + x_key * (abs(x_dist) - 1)
        else:
            start_move = '^'
            mov_s = y_key * (abs(y_dist) - 1) + x_key * abs(x_dist)
    else:
        mov_s = y_key * abs(y_dist) + x_key * abs(x_dist)

    possible_inputs = [
        f"{start_move}{''.join(x)}A"
        for x in set(permutations(mov_s))
    ]

    min_score = maxsize
    min_input = ""
    for inputs in possible_inputs:
        score = dir_solve(inputs, 25)
        if score < min_score:
            min_score = score
            min_input = inputs

    return min_input

def solve(code):
    total = 0
    for start, end in pairwise(f"A{code}"):
        total += dir_solve(num_solve(start, end), 25)
        print(start, end)
    return total

total = 0
sequences = []
for code in input.split('\n'):
    if code.strip() == '':
        continue

    minlen = solve(code)
    val = int(code[:3])
    print(code, minlen, val, minlen * val)
    total += minlen * val

print(total)
