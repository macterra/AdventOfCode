# https://adventofcode.com/2024/day/21

from itertools import product

numpad = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    ' ': (3, 0), '0': (3, 1), 'A': (3, 2)
}

keypad = {
    ' ': (0, 0), '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

input = """
029A
980A
179A
456A
379A
"""

def genPath(pad, start, finish, rowFirst):
    r1, c1 = pad[start]
    r2, c2 = pad[finish]
    path = ''

    while (r1, c1) != (r2, c2):
        if (r1, c1) == pad[' ']:
            return None
        #print(r1, c1, r2, c2)
        if rowFirst:
            if r2 < r1:
                path += "^"
                r1 -= 1
                continue
            if r2 > r1:
                path += 'v'
                r1 += 1
                continue
            if c2 < c1:
                path += '<'
                c1 -= 1
                continue
            if c2 > c1:
                path += ">"
                c1 += 1
                continue
        else:
            if c2 < c1 and (r1, c1-1):
                path += '<'
                c1 -= 1
                continue
            if c2 > c1:
                path += ">"
                c1 += 1
                continue
            if r2 < r1:
                path += "^"
                r1 -= 1
                continue
            if r2 > r1:
                path += 'v'
                r1 += 1
                continue
    return path

def genPaths(pad, start, finish):
    path1 = genPath(pad, start, finish, True)
    path2 = genPath(pad, start, finish, False)

    paths = []
    if path1 is not None:
        paths.append(path1 + 'A')

    if path2 is not None and path2 != path1:
        paths.append(path2 + 'A')

    return paths

def genSequence(pad, code):
    start = 'A'
    segments = []
    for x in code:
        paths = genPaths(pad, start, x)
        segments.append(paths)
        start = x
    return [''.join(parts) for parts in product(*segments)]


input = open('data', 'r').read()
total = 0
sequences = []
for code in input.split('\n'):
    if code.strip() == '':
        continue

    seqs = genSequence(numpad, code)

    robot1 = []
    for seq in seqs:
        robot1 += genSequence(keypad, seq)

    robot2 = []
    for seq in robot1:
        robot2 += genSequence(keypad, seq)

    minlen = min([len(seq) for seq in robot2])
    val = int(code[:3])
    print(code, minlen, val, minlen * val)
    total += minlen * val
print(total)

