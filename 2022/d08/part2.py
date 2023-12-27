import numpy as np

data = """30373
25512
65332
33549
35390"""

def makeGrid(lines):
    w = len(lines[0])
    h = len(lines)
    grid = np.full((h,w), 0)
    for i in range(h):
        for j in range(w):
            grid[i,j] = int(lines[i][j])
    return grid

def isVisible(grid, i, j):
    ht = grid[i,j]
    up = grid[:,j][:i]
    dn = grid[:,j][i+1:]
    lt = grid[i,:][:j]
    rt = grid[i,:][j+1:]

    return max(up) < ht or max(dn) < ht or max(lt) < ht or max(rt) < ht

def scenicScore(grid, i, j):
    ht = grid[i,j]
    up = np.flip(grid[:,j][:i])
    dn = grid[:,j][i+1:]
    lt = np.flip(grid[i,:][:j])
    rt = grid[i,:][j+1:]

    ud = 0
    for h in up:
        ud += 1
        if h >= ht:
            break

    dd = 0
    for h in dn:
        dd += 1
        if h >= ht:
            break

    ld = 0
    for h in lt:
        ld += 1
        if h >= ht:
            break

    rd = 0
    for h in rt:
        rd += 1
        if h >= ht:
            break

    return ud*dd*ld*rd

data = open('data', 'r').read()
lines = data.split('\n')
grid = makeGrid(lines)
w, h = grid.shape
print(grid)

best = 0
for i in range(1,h-1):
    for j in range(1,w-1):
        score = scenicScore(grid, i, j)
        if score > best:
            best = score
print(best)
