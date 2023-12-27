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
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1


    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

    def notDiagonal(self):
        return self.x1 == self.x2 or self.y1 == self.y2

lines = []
for spec in input:
    line = Line(spec)
    if line.notDiagonal():
        lines.append(line)

w = 0
h = 0
for line in lines:
    maxX = max([line.x1, line.x2])
    maxY = max([line.y1, line.y2])
    if maxX > w:
        w = maxX
    if maxY > h:
        h = maxY

print(w, h)

grid = np.zeros((w+1,h+1))

for line in lines:
    for x in range(line.x1, line.x2+1):
        for y in range(line.y1, line.y2+1):
            grid[y,x] += 1

print(grid)
print(len(grid[grid>1]))
