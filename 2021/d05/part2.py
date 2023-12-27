import numpy as np

input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

input = open('data', 'r').read()
input = input.split('\n')

print(input)

class Line:
    def __init__(self, line):
        points = line.split(" -> ")
        #print(points)
        x1, y1 = points[0].split(',')
        x2, y2 = points[1].split(',')
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

lines = [Line(spec) for spec in input]

w = 0
h = 0
for line in lines:
    w = max([w, line.x1, line.x2])
    h = max([h, line.y1, line.y2])

print(w, h)

grid = np.zeros((w+1,h+1))

for line in lines:
    print(line)
    x = line.x1
    y = line.y1
    grid[y,x] += 1
    while x != line.x2 or y != line.y2:
        if line.x2 > x:
            x += 1
        if line.x2 < x:
            x -= 1
        if line.y2 > y:
            y += 1
        if line.y2 < y:
            y -= 1
        grid[y,x] += 1

print(grid)
print(len(grid[grid>1]))
