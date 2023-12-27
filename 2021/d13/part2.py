import numpy as np

input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

input = open('data', 'r').read()

def makePaper(input):
    lines = input.split('\n')
    points = []
    xmax = 0
    ymax = 0
    for i in range(len(lines)):
        line = lines[i]
        if len(line) == 0:
            break
        x, y = line.split(',')
        x = int(x)
        y = int(y)
        xmax = max(xmax, x)
        ymax = max(ymax, y)
        points.append((x,y))
        print(f"x={x} y={y}")

    print(points, xmax, ymax)
    paper = np.full((ymax+1, xmax+1), 0)
    for x,y in points:
        paper[y,x] = 1

    folds = []
    for line in lines[i+1:]:
        dir, val = line.split('=')
        print(dir, val)
        folds.append((dir[-1:], int(val)))

    return paper, folds

paper, folds = makePaper(input)
print(paper)
print(folds)

def foldPaper(paper, fold):
    dir, axis = fold
    print(f"dir={dir} axis={axis}")

    if dir == 'y':
        print("fold ud")
        top = paper[:axis,]
        bottom = paper[axis+1:,]
        flipped = np.flipud(bottom)

        th, _ = top.shape
        bh, _ = bottom.shape

        print(top,top.shape)
        print(bottom, bottom.shape)
        print(flipped, flipped.shape)
        top[th-bh:,] += flipped
        return(top)
    else:
        print("fold lr")
        print(paper, paper.shape)
        left = paper[...,:axis]
        right = paper[...,axis+1:]

        _, lw = left.shape

        print(left, left.shape)
        print(right, right.shape)
        flipped = np.fliplr(left)
        print(flipped)
        right[...,0:lw] += flipped
        return(right)

for fold in folds:
    paper = foldPaper(paper, fold)
    print(paper, paper.shape)

paper = np.fliplr(paper)
h, w = paper.shape 

for i in range(h):
    for j in range(w):
        if paper[i,j] > 0:
            print('X', end='')
        else:
            print('.', end='')
    print()