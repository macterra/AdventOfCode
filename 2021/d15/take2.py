import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

input1 = """392
721
413"""

input2 = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

input3 = """18888
18111
18181
18181
11181"""

input4 = open('data', 'r').read()

def makeGrid(input):
    grid = []
    lines = input.split('\n')
    for line in lines:
        grid.append([int(n) for n in line])
    return grid

def makeGraph(grid):    
    w = len(grid[0])
    h = len(grid)

    sz = w * h
    print(f"w={w} h={h} sz={sz}")
    graph = np.zeros((sz,sz))

    # print(graph)

    for i in range(h):
        for j in range(1, w):
            print(i, j, grid[i][j])
            n1 = i*w + j
            n2 = i*w + j - 1
            graph[n1, n2] = grid[i][j]

    for j in range(w):
        for i in range(1, h):
            print(i, j, grid[i][j])
            n1 = (i-1)*w + j
            n2 = i*w + j
            graph[n1, n2] = grid[i][j]

    return csr_matrix(graph)

def printPath(predecessors):
    print(predecessors)
    n = predecessors[-1]
    path = []
    ht = len(grid)
    width = len(grid[0])
    while n >= 0:
        i = n%width
        j = n//width
        c = (j, i)
        path.append(c)
        #print(n, c)
        n = predecessors[n]
    path.reverse()
    path.append((ht-1,width-1)) 
    print(path)
    print(len(path))  

    risk = 0
    for i, j in path[1:]:
        risk += grid[i][j]
        print((i, j), grid[i][j], risk)

grid = makeGrid(input4)
print(grid, len(grid))
graph = makeGraph(grid)
print(graph, graph.shape[0])

dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, indices=0, return_predecessors=True)

print(dist_matrix)
printPath(predecessors)

# for i in range(len(predecessors)):
#     print(i, predecessors[i])

print(dist_matrix[-1])