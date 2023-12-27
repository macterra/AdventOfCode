import numpy as np

input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

input = open('data', 'r').read()

lines = input.split('\n')

def makeRules(line):
    print(line)
    rules = []
    for c in line:
        if c == '#':
            rules.append(1)
        else:
            rules.append(0)
    return rules

def makeGrid(lines):
    w = len(lines[0])
    h = len(lines)
    #print(lines, w, h)
    grid = np.full((h+4,w+4), 0)
    for i in range(h):
        for j in range(w):
            if lines[i][j] == '#':
                grid[i+2,j+2] = 1
    return grid

def region(grid, i, j):
    #print(i, j, grid[i,j])
    reg = grid[i-1:i+2,j-1:j+2]
    reg = np.reshape(reg, (9,))
    reg = "".join([str(v) for v in reg])
    reg = int(reg, 2)
    #print(reg)
    return reg

def step(grid, rules):
    w, h = grid.shape
    print(f"step {w} {h}")

    if grid[0,0] == 0:
        init = rules[0]
    else:
        init = rules[511]

    next = np.full((h+2,w+2), init)
    print(grid[0,0], rules[0], rules[255], init)
    printGrid(next)

    for i in range(1,h-1):
        for j in range(1,w-1):
            k = region(grid, i, j)
            next[i+1,j+1] = rules[k]
    return next

def printGrid(grid):
    for row in grid:
        for v in row:
            if v == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print(len(grid[grid==1]))

rules = makeRules(lines[0])
print(rules, len(rules))

grid = makeGrid(lines[2:])
printGrid(grid)

for i in range(50):
    grid = step(grid, rules)
    printGrid(grid)

