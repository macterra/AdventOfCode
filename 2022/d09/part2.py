data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

def parse(lines):
    motions = []
    for line in lines:
        d, n = line.split(' ')
        motions.append((d, int(n)))
    return motions

data = open('data', 'r').read()
lines = data.split('\n')
motions = parse(lines)


rope = [(0,0) for i in range(10)]
allT = { (0,0): True }

moves = {
    'R': (+1, 0),
    'L': (-1, 0),
    'U': (0, +1),
    'D': (0, -1)
}

updates = {
    (-2, -2): (-1, -1),
    (-2, -1): (-1, -1),
    (-2, 0): (-1, 0),
    (-2, 1): (-1, 1),
    (-2, 2): (-1, 1),

    (2, -2): (1, -1),
    (2, -1): (1, -1),
    (2, 0): (1, 0),
    (2, 1): (1, 1),
    (2, 2): (1, 1),

    (-2, 2): (-1, 1),
    (-1, 2): (-1, 1),
    (0, 2): (0, 1),
    (1, 2): (1, 1),
    (2, 2): (1, 1),

    (-2, -2): (-1, -1),
    (-1, -2): (-1, -1),
    (0, -2): (0, -1),
    (1, -2): (1, -1),
    (2, -2): (1, -1)
}

def stayClose(H, T):
    hx, hy = H
    tx, ty = T
    pos = (hx-tx, hy-ty)

    if pos in updates:
        dx, dy = updates[pos]
        tx += dx
        ty += dy

    return (tx, ty)

print(rope)
for motion in motions:
    print(motion)
    d, n = motion
    for i in range(n):
        x, y = rope[0]
        dx, dy = moves[d]
        rope[0] = (x+dx, y+dy)
        for j in range(1,10):
            rope[j] = stayClose(rope[j-1], rope[j])
        allT[rope[-1]] = True
    print(rope)

print(len(allT))
