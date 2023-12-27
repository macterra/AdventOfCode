import numpy as np
import re

data = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

class Map:
    def __init__(self, lines):
        w = max([len(line) for line in lines])
        h = len(lines)
        grid = np.full((h,w), ' ')
        for i in range(h):
            for j in range(len(lines[i])):
                grid[i,j] = lines[i][j]
        self.grid = grid
        self.x = min(np.where(self.grid[0,] == '.')[0])
        self.y = 0
        self.face = '>'
        self.trace = np.copy(self.grid)
        self.trace[self.y, self.x] = self.face

    def __repr__(self) -> str:
        h, w = self.grid.shape
        out = ""
        for row in range(h):
            out += "".join(self.trace[row,:]) + '\n'
        return out

    def followPath(self, path):
        directions = re.findall("(\d+)([LR])", path)
        self.directions = [ (int(x), y) for x, y in directions]
        print(self.directions)

        for dis, dir in self.directions:
            self.move(dis)
            self.turn(dir)
            print(self)

        match = re.search(r"(\d+)$", path)
        print(path, match)
        if match:
            dis = int(match.group(1))
            self.move(dis)
            print(self)

    def move(self, dis):
        h, w = self.grid.shape
        deltas = { '>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1) }
        dx, dy = deltas[self.face]

        print('move', dis, dx, dy)

        for i in range(dis):
            ny, nx = (self.y + dy)%h, (self.x + dx)%w
            next = self.grid[ny, nx]
            if next == '#':
                break
            elif next == ' ':
                nx, ny = self.wrap()
                next = self.grid[ny, nx]
                if next == '#':
                    break
                else:
                    self.x, self.y = nx, ny
            else:
                self.x += dx
                self.y += dy
            self.trace[self.y, self.x] = self.face

    def wrap(self):
        if self.face == '>':
            nx = min(np.where(self.grid[self.y,:] != ' ')[0])
            ny = self.y
        elif self.face == '<':
            nx = max(np.where(self.grid[self.y,:] != ' ')[0])
            ny = self.y
        elif self.face == '^':
            ny = max(np.where(self.grid[:,self.x] != ' ')[0])
            nx = self.x
        elif self.face == 'v':
            ny = min(np.where(self.grid[:,self.x] != ' ')[0])
            nx = self.x

        return nx, ny

    def turn(self, dir):
        print('turn', dir)
        if dir not in ['R', 'L']:
            raise "nope"

        if self.face == '>':
            if dir == 'R':
                self.face = 'v'
            else:
                self.face = '^'
        elif self.face == '<':
            if dir == 'R':
                self.face = '^'
            else:
                self.face = 'v'
        elif self.face == '^':
            if dir == 'R':
                self.face = '>'
            else:
                self.face = '<'
        elif self.face == 'v':
            if dir == 'R':
                self.face = '<'
            else:
                self.face = '>'
                
        self.trace[self.y, self.x] = self.face

    def password(self):
        bonus = { '>': 0, 'v': 1, '<': 2, '^': 3}
        return (self.y+1) * 1000 + (self.x+1) * 4 + bonus[self.face]

data = open('data', 'r').read()
grid, path = data.split('\n\n')
lines = grid.split('\n')
map = Map(lines)
print(map.grid.shape)
map.followPath(path)
print(map.x+1, map.y+1)
print(map.password())
