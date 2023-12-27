import numpy as np
from collections import defaultdict

data = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""

def parse(lines):
    elves = set()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                elves.add((j, i))

    return elves

def makeGrid(elves):
    minx = min([x for x, y in elves])
    miny = min([y for x, y in elves])
    maxx = max([x for x, y in elves])
    maxy = max([y for x, y in elves])
    #print(minx, miny, maxx, maxy)

    h = maxy-miny+1
    w = maxx-minx+1

    grid = np.full((h,w), '.')

    for x, y in elves:
        grid[y-miny,x-minx] = '#'

    return grid

def displayGrid(elves):
    grid = makeGrid(elves)
    h, w = grid.shape
    for row in range(h):
        print("".join(grid[row,]))

directions = list("NSWE")

def jump(elves):
    #print(directions)

    locations = defaultdict(list)

    for x, y in elves:
        nn = ns = nw = ne = 0

        for d in directions:
            if d == 'N':
                for dx in [-1, 0, 1]:
                    if (x+dx, y-1) in elves:
                        nn += 1
            elif d == 'S':
                for dx in [-1, 0, 1]:
                    if (x+dx, y+1) in elves:
                        ns += 1
            elif d == 'W':
                for dy in [-1, 0, 1]:
                    if (x-1, y+dy) in elves:
                        nw += 1
            elif d == 'E':
                for dy in [-1, 0, 1]:
                    if (x+1, y+dy) in elves:
                        ne += 1

        #print(x, y, nn, ns, nw, ne)
        if (nn+ns+nw+ne) == 0:
            continue

        for d in directions:
            if d == 'N' and nn == 0:
                locations[(x, y-1)].append((x, y))
                break
            elif d == 'S' and ns == 0:
                locations[(x, y+1)].append((x, y))
                break
            elif d == 'W' and nw == 0:
                locations[(x-1, y)].append((x, y))
                break
            elif d == 'E' and ne == 0:
                locations[(x+1, y)].append((x, y))
                break

    for target in locations:
        #print(target, locations[target])
        next = locations[target]
        if len(next) == 1:
            elves.add(target)
            elves.remove(next[0])

    directions.append(directions.pop(0))
    return elves

data = open('data', 'r').read()
lines = data.split('\n')
elves = parse(lines)
print(elves)
print("== Initial State ==")
displayGrid(elves)

for i in range(10):
    elves = jump(elves)
    print()
    print("== End of Round {} ==".format(i+1))
    displayGrid(elves)

grid = makeGrid(elves)
empty = np.where(grid == '.')
print(len(empty[0]))
