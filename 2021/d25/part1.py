import numpy as np

input = """...>...
.......
......>
v.....>
......>
.......
..vvv.."""

input="""v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

def makeGrid(input):
    lines = input.split('\n')
    h = len(lines)
    w = len(lines[0])

    grid = np.full((h,w), '.')
    for i in range(h):
        for j in range(w):
            grid[i,j] = lines[i][j]
    return grid

def step(grid):
    h, w = grid.shape

    for y in range(h):
        for x in range(w):
            if grid[y,x] == '.':         
                if grid[y,x-1] == '>':
                    grid[y,x-1] = 'e'

    next = np.full((h,w), '.')

    for y in range(h):
        for x in range(w):
            if grid[y,x-1] == 'e':
                next[y,x] = '>'
            elif grid[y,x] == 'e':
                next[y,x] = '.'
            else:
                next[y,x] = grid[y,x]

    grid = next
    
    for y in range(h):
        for x in range(w):
            if grid[y,x] == '.':         
                if grid[y-1,x] == 'v':
                    grid[y-1,x] = 's'

    next = np.full((h,w), '.')

    for y in range(h):
        for x in range(w):
            if grid[y-1,x] == 's':
                next[y,x] = 'v'
            elif grid[y,x] == 's':
                next[y,x] = '.'
            else:
                next[y,x] = grid[y,x]

    return next            

def printGrid(grid):
    for row in grid:
        print("".join(list(row)))

input = open('data', 'r').read()
grid = makeGrid(input)

print(f"initial")
printGrid(grid)

i = 0
while True:
    i += 1
    print(f"after {i} steps")
    next = step(grid)
    printGrid(next)
    if np.array_equal(next, grid):
        print(f"stopped after {i}")
        break
    grid = next
