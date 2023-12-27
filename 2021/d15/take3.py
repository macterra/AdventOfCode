import astar

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

input3 = """18888
18111
18181
18181
11181"""

class ShortPath(astar.AStar):
    def __init__(self, input):
        print(input)
        grid = []
        lines = input.split('\n')
        for line in lines:
            grid.append([int(n) for n in line])
        print(grid)            
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])

    def neighbors(self, node):
        x, y = self.node2coord(node)
        print(f"neighbors {node} {x} {y}")

        near = []

        if x == 0:
            near.append(self.coord2node(x+1, y))
        elif x == self.w-1:            
            near.append(self.coord2node(x-1, y))
        else:
            near.append(self.coord2node(x+1, y))
            near.append(self.coord2node(x-1, y))

        if y == 0:
            near.append(self.coord2node(x, y+1))
        elif y == self.h-1:            
            near.append(self.coord2node(x, y-1))
        else:
            near.append(self.coord2node(x, y+1))
            near.append(self.coord2node(x, y-1))

        return near

    def distance_between(self, n1, n2):
        x, y = self.node2coord(n2)
        return self.grid[y][x]

    def heuristic_cost_estimate(self, current, goal):
        x1, y1 = self.node2coord(current) 
        x2, y2 = self.node2coord(goal)
        dx = x1-x2
        dy = y1-y2
        return dx*dx + dy*dy

    def heuristic_cost_estimate2(self, current, goal):
        x, y = self.node2coord(current) 
        x2, y2 = self.node2coord(goal)
        cost = 0
        while x != x2 and y != y2:
            if x < x2:
                x += 1
            if x > x2:
                x -= 1    
            cost += self.grid[y][x]

            if y < y2:
                y += 1
            if y > y2:
                y -= 1
            cost += self.grid[y][x]

        print(f"cost estimate {current}->{goal}={cost}")    
        return cost         

    def node2coord(self, node):
        return node%self.w, node//self.w

    def coord2node(self, x, y):
        return y*self.w + x

    def findPath(self):
        goal = self.w * self.h - 1
        path = self.astar(0, goal)
        cost = 0
        if path:
            path = list(path)
            for i in range(1, len(path)):
                cost += self.distance_between(path[i-1], path[i])
        self.path = [self.node2coord(n) for n in path]
        self.cost = cost
        return path

sp = ShortPath(input3)
near = sp.neighbors(16)
print(near)
print(sp.distance_between(26, 16))
print(sp.findPath())
print(f"cost={sp.cost}")
print(sp.path)
