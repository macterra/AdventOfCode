# https://adventofcode.com/2023/day/24

import sympy

data = r"""
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

def parse(data):
    stones = []
    for line in data.strip().split('\n'):
        loc, vel = line.split(' @ ')
        x, y, z = [int(val) for val in loc.split(', ')]
        dx, dy, dz = [int(val) for val in vel.split(', ')]
        stones.append(([x, y, z, dx, dy, dz]))
    return stones

data = open('data', 'r').read()
stones = parse(data)
print(stones)

sx, sy, sz, sdx, sdy, sdz = sympy.symbols("sx, sy, sz, sdx, sdy, sdz")
equations = []

i = 0
for stone in stones:
    i += 1
    x, y, z, dx, dy, dz = stone
    equations.append((sx - x) * (dy - sdy) - (sy - y) * (dx - sdx))
    equations.append((sy - y) * (dz - sdz) - (sz - z) * (dy - sdy))

    if i < 2:
        continue

    ans = sympy.solve(equations)
    if all(x % 1 == 0 for solution in ans for x in solution.values()):
        ans = ans[0]
        print(ans)
        print(ans[sx] + ans[sy] + ans[sz])
        break

# h/t https://github.com/xHyroM/
