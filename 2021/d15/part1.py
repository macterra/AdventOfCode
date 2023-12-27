import numpy as np

input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

# input = """18888
# 18111
# 18181
# 18181
# 11181"""

#input = open('data', 'r').read()

def makeGrid(input):    
    lines = input.split('\n')
    w = len(lines[0])
    h = len(lines)

    #print(lines, w, h)

    grid = np.full((w+2,h+2), 99)

    for i in range(h):
        for j in range(w):
            grid[i+1, j+1] = int(lines[i][j])

    return grid

omega = 999999
N = 0

def tryPath(grid, path, next, risk, minRisk):
    global N
    N += 1

    if N % 1000000 == 0:
        print(f"{N} try {len(path)} {next} {risk} {minRisk}")

    # if next in path:
    #     return omega

    if grid[next] == 99:
        return omega

    h, w = grid.shape
    i, j = next

    risk += grid[i,j]
    if risk > minRisk:
        return omega

    path.append(next)
    #print(path, risk)

    if i == h-2 and j == w-2:
        return risk

    if grid[i, j+1] < grid[i+1, j]:
        a = tryPath(grid, path.copy(), (i, j+1), risk, minRisk)
        minRisk = min(a, minRisk)
        b = tryPath(grid, path.copy(), (i+1, j), risk, minRisk)
    else:
        a = tryPath(grid, path.copy(), (i+1, j), risk, minRisk)
        minRisk = min(a, minRisk)
        b = tryPath(grid, path.copy(), (i, j+1), risk, minRisk)

    #minRisk = min(b, minRisk)
    # c = tryPath(grid, path.copy(), (i, j-1), risk, minRisk)
    # minRisk = min(c, minRisk)
    # d = tryPath(grid, path.copy(), (i-1, j), risk, minRisk)

    return min(a, b) #, c, d)    

grid = makeGrid(input)
print(grid)

risk = tryPath(grid, [], (1,1), 0, omega)
print(N, risk-grid[1,1])
