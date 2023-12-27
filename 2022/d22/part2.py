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

class Cube:
    def __init__(self) -> None:
        pass
    
    def read(self, map):
        print(map.grid.shape)
        print(map)
        self.map = map
        h, w = map.grid.shape
        self.tile = 'A'
        self.x = 0
        self.y = 0
        self.face = '>'
        self.crossed = set()

        if w > h:
            self.tsize = ts = w//4
            self.tiles = np.full((3,4,ts,ts), ' ')
            for row in range(3):
                for col in range(4):
                    self.tiles[row, col] = map.grid[row*ts:(row+1)*ts,col*ts:(col+1)*ts]
                    print(row, col)
                    print(self.tiles[row, col])
            row = 0
            col = map.x//ts
            self.faces = {
                'A': self.tiles[row,col],
                'B': self.tiles[row+1,col-1],
                'C': self.tiles[row+1,col],
                'D': np.rot90(self.tiles[row+2,col+1]),
                'E': self.tiles[row+2,col],
                'F': np.rot90(self.tiles[row+1,col-2],2)
            }
            self.invfaces = {
                'A': (row,col,0),
                'B': (row+1,col-1,0),
                'C': (row+1,col,0),
                'D': (row+2,col+1,1),
                'E': (row+2,col,0),
                'F': (row+1,col-2,2)
            }
        else:
            self.tsize = ts = h//4
            self.tiles = np.full((4,3,ts,ts), ' ')
            for row in range(4):
                for col in range(3):
                    self.tiles[row, col] = map.grid[row*ts:(row+1)*ts,col*ts:(col+1)*ts]
            row = 0
            col = map.x//ts
            self.faces = {
                'A': self.tiles[row,col],
                'B': np.rot90(self.tiles[row+2,col-1],3),
                'C': self.tiles[row+1,col],
                'D': np.rot90(self.tiles[row,col+1], 3),
                'E': self.tiles[row+2,col],
                'F': np.rot90(self.tiles[row+3,col-1],1)
            }
            self.invfaces = {
                'A': (row,col,0),
                'B': (row+2,col-1,3),
                'C': (row+1,col,0),
                'D': (row,col+1,3),
                'E': (row+2,col,0),
                'F': (row+3,col-1,1)
            }

    def followPath(self, path):
        print(path)
        
        directions = re.findall("(\d+)([LR])", path)
        self.directions = [ (int(x), y) for x, y in directions]
        print(self.directions)

        for dis, dir in self.directions:
            self.move(dis)
            self.turn(dir)
            print(self.x, self.y, self.face, self.tile)
            
        match = re.search(r"(\d+)$", path)
        print(path, match)
        if match:
            dis = int(match.group(1))
            self.move(dis)
            
        print('final', self.x, self.y, self.face, self.tile, self.map.password())
        print(sorted(self.crossed))
            
    def move(self, dis):
        ts = self.tsize
        deltas = { '>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1) }
        dx, dy = deltas[self.face]
        grid = self.faces[self.tile]

        print('move', dis, dx, dy)

        for i in range(dis):
            ny, nx = (self.y + dy), (self.x + dx)

            if not (0 <= nx < ts and 0 <= ny < ts):
                self.crossed.add(self.tile + self.face)
                self.x, self.y, self.face, self.tile = self.wrap()
                grid = self.faces[self.tile]
                dx, dy = deltas[self.face]
            else:
                next = grid[ny, nx]
                if next == '#':
                    break
                else:
                    self.x += dx
                    self.y += dy

            row, col, rot = self.invfaces[self.tile]
            x = col*ts + self.x
            y = row*ts + self.y
            self.map.x = x
            self.map.y = y
            self.map.face = self.face
            self.map.trace[y, x] = self.face
            #print(self.map)
    
    def wrap(self):
        """        
        A 
            N: FS
            S: CN
            E: DN*
            W: BN
        B 
            N: AW
            S: EW*
            E: CW
            W: FW*
        C 
            N: AS
            S: EN 
            E: DW
            W: BE
        D 
            N: AE*
            S: EE
            E: FE*
            W: CE
        E 
            N: CS
            S: FN
            E: DS
            W: BS*
        F 
            N: ES
            S: AN
            E: DE*
            W: BW*
        """

        edge = self.tsize-1
        nx = self.x
        ny = self.y
        nf = self.face

        if self.tile == 'A':
            if self.face == '^':
                nt = 'F' #FS
                ny = edge
            elif self.face == 'v':
                nt = 'C' #CN
                ny = 0
            elif self.face == '>':
                nt = 'D' #DN*
                nx = edge-self.y
                ny = 0
                nf = 'v'
            elif self.face == '<':
                nt = 'B' #BN
                nx = self.y
                ny = 0
                nf = 'v'
        elif self.tile == 'B':
            if self.face == '^':
                nt = 'A' #AW
                nx = 0
                ny = self.x
                nf = '>'
            elif self.face == 'v':
                nt = 'E' #EW*
                nx = 0
                ny = edge-self.x
                nf = '>'
            elif self.face == '>':
                nt = 'C' #CW
                nx = 0
                nf = '>'
            elif self.face == '<':
                nt = 'F' #FW*
                nx = 0
                ny = edge-self.y
                nf = '>'
        elif self.tile == 'C':
            if self.face == '^':
                nt = 'A' #AS
                ny = edge
            elif self.face == 'v':
                nt = 'E' #EN
                ny = 0
            elif self.face == '>':
                nt = 'D' #DW
                nx = 0
            elif self.face == '<':
                nt = 'B' #BE
                nx = edge
        elif self.tile == 'D':
            if self.face == '^':
                nt = 'A' # AE*
                nx = edge
                ny = edge-self.x
                nf = '<'
            elif self.face == 'v':
                nt = 'E' #EE
                nx = edge
                ny = self.x
                nf = '<'
            elif self.face == '>':
                nt = 'F' #FE*
                nx = edge
                ny = edge-self.y
                nf = '<'
            elif self.face == '<':
                nt = 'C' #CE
                nx = edge
                nf = '<'
        elif self.tile == 'E':
            if self.face == '^':
                nt = 'C' #CS                
                ny = edge
            elif self.face == 'v':
                nt = 'F' #FN
                ny = 0
            elif self.face == '>':
                nt = 'D' #DS
                nx = self.y
                ny = edge
                nf = '^'
            elif self.face == '<':
                nt = 'B' #BS*
                nx = edge-self.y
                ny = edge
                nf = '^'
        elif self.tile == 'F':
            if self.face == '^':
                nt = 'E' #ES
                ny = edge
                nf = '^'
            elif self.face == 'v':
                nt = 'A' #AN
                ny = 0
            elif self.face == '>':
                nt = 'D' #DE*
                nx = edge
                ny = edge-self.y
                nf = '<'
            elif self.face == '<':
                nt = 'B' #BW*
                nx = 0
                ny = edge-self.y
                nf = '>'
        
        if self.faces[nt][ny,nx] == '#':
            return self.x, self.y, self.face, self.tile
        else:
            return nx, ny, nf, nt

    def turn(self, dir):
        self.map.face = self.face
        self.map.turn(dir)
        self.face = self.map.face

data = open('data', 'r').read()
grid, path = data.split('\n\n')
lines = grid.split('\n')
map = Map(lines)
cube = Cube()
cube.read(map)
cube.followPath(path)
