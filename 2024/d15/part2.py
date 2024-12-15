# https://adventofcode.com/2024/day/15

import numpy as np

test1 = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""

test2 = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

#input = test1
#input = test2
input = open('data', 'r').read()

def makeGrid(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    w = len(lines[0]) * 2
    h = len(lines)
    grid = np.full((h,w), '.')
    for i in range(h):
        for j in range(w//2):
            cell = lines[i][j]
            if cell == '#':
                grid[i,2*j] = '#'
                grid[i,2*j+1] = '#'
            elif cell == '@':
                grid[i,2*j] = '@'
                grid[i,2*j+1] = '.'
            elif cell == 'O':
                grid[i,2*j] = '['
                grid[i,2*j+1] = ']'
            elif cell == '.':
                grid[i,2*j] = '.'
                grid[i,2*j+1] = '.'
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

def parseInput(input):
    warehouse, moves = input.split('\n\n')
    grid = makeGrid(warehouse)
    moves = [x for x in moves if x != '\n']
    return grid, moves

grid, moves = parseInput(input)
printGrid(grid)
#print(moves)

def push(loc, move):
    global grid
    obj = grid[loc]
    i, j = loc

    if obj == '@' or move == '<' or move == ">":
        if move == '^':
            dst = (i-1, j)
        elif move == 'v':
            dst = (i+1, j)
        elif move == '>':
            dst = (i, j+1)
        elif move == '<':
            dst = (i, j-1)

        cell = grid[dst]
        if cell == '#':
            return False
        if cell == '.' or push(dst, move):
            grid[dst] = grid[loc]
            grid[loc] = '.'
            return True
        return False

    if obj == '[':
        src1 = (i, j)
        src2 = (i, j+1)
        if move == '^':
            dst1 = (i-1, j)
            dst2 = (i-1, j+1)
        elif move == 'v':
            dst1 = (i+1, j)
            dst2 = (i+1, j+1)
    elif obj == ']':
        src1 = (i, j-1)
        src2 = (i, j)
        if move == '^':
            dst1 = (i-1, j-1)
            dst2 = (i-1, j)
        elif move == 'v':
            dst1 = (i+1, j-1)
            dst2 = (i+1, j)

    if grid[dst1] == '#' or grid[dst2] == '#':
        return False

    backup = grid.copy()
    if (grid[dst1] == '.' or push(dst1, move)) and (grid[dst2] == '.' or push(dst2, move)):
        grid[dst1] = '['
        grid[dst2] = ']'
        grid[src1] = '.'
        grid[src2] = '.'
        return True
    grid = backup
    return False


for move in moves:
    ys, xs = np.where(grid == '@')
    loc = list(zip(ys, xs))[0]
    #print(loc)
    push(loc, move)
    #printGrid(grid)

ys, xs = np.where(grid == '[')
boxes = list(zip(ys, xs))
total = 0
for box in boxes:
    i, j = box
    total += 100 * i + j
print(total)
