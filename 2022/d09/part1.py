data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

def parse(lines):
    motions = []
    for line in lines:
        d, n = line.split(' ')
        motions.append((d, int(n)))
    return motions

data = open('data', 'r').read()
lines = data.split('\n')
motions = parse(lines)

H = (0,0)
T = (0,0)
allT = { T: True }

moves = {
    'R': (+1, 0),
    'L': (-1, 0),
    'U': (0, +1),
    'D': (0, -1)
}

updates = {
    (-2, -1): (-1, -1),
    (-2, 0): (-1, 0),
    (-2, 1): (-1, 1),
    (2, -1): (1, -1),
    (2, 0): (1, 0),
    (2, 1): (1, 1),
    (-1, 2): (-1, 1),
    (0, 2): (0, 1),
    (1, 2): (1, 1),
    (-1, -2): (-1, -1),
    (0, -2): (0, -1),
    (1, -2): (1, -1)
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

for motion in motions:
    d, n = motion
    for i in range(n):
        x, y = H
        dx, dy = moves[d]
        H = (x+dx, y+dy)
        T = stayClose(H, T)
        allT[T] = True

print(len(allT))