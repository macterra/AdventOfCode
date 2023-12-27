import numpy as np

data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

def parse(lines):
    paths = []
    for line in lines:
        points = line.split(' -> ')
        path = []
        for point in points:
            x, y = point.split(',')
            path.append((int(x), int(y)))
        paths.append(path)
    return paths

def makeGrid(paths):
    #print(paths)
    rows = 0
    cols = 0
    minx = 10000
    miny = 10000
    for path in paths:
        for x,y in path:
            cols = max(cols, x)
            rows = max(rows, y)
            minx = min(minx, x)
            miny = min(miny, y)

    rows += 2
    cols += 500
    #print(rows)
    grid = np.full((rows+1,cols+1), '.')

    for path in paths:
        for i in range(len(path)-1):
            x1, y1 = path[i]
            x2, y2 = path[i+1]
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            grid[y1:y2+1,x1:x2+1] = '#'

    grid[rows:,] = '#'

    return grid, 0, miny

data = open('data', 'r').read()
lines = data.split('\n')
paths = parse(lines)
grid, minx, miny = makeGrid(paths)
print(grid.shape)
print(minx, miny)

#grid[0:1,500:501] = '+'

def printGrid(grid, minx):
    w,h = grid.shape
    for row in range(w):
        print("{:04d}".format(row), "".join(grid[row,:][minx:]))

def drop(grid, x, y):
    h, w = grid.shape
    y += 1

    if grid[y:y+1,x:x+1] == 'o':
        return False

    if grid[y+1:y+2,x:x+1] == '.':
        return drop(grid, x, y)

    if grid[y+1:y+2,x-1:x] == '.':
        return drop(grid, x-1, y)

    if grid[y+1:y+2,x+1:x+2] == '.':
        return drop(grid, x+1, y)

    grid[y:y+1,x:x+1] = 'o'
    return True

grains = 0
while drop(grid, 500, -1):
    grains += 1
    #print(grains)

printGrid(grid, minx)
print(grains)
