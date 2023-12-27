data = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

class Brick:
    def __init__(self, spec):
        self.spec = spec
        a, b = spec.split('~')

        x1, y1, z1 = [int(val) for val in a.split(',')]
        x2, y2, z2 = [int(val) for val in b.split(',')]

        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        z1, z2 = min(z1, z2), max(z1, z2)

        self.dx = x2 - x1 + 1
        self.dy = y2 - y1 + 1
        self.dz = z2 - z1 + 1

        self.cubes = []
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    self.cubes.append((x,y,z))

        self.height = z1

    def __repr__(self):
        return f"Brick ({self.dx}x{self.dy}x{self.dz} at {self.height})"

    def copy(self):
        other = Brick(self.spec)
        other.cubes = [cube for cube in self.cubes]
        other.height = self.height
        return other

    def canDrop(self, stack):
        for x, y, z in self.cubes:
            if z == 1:
                return False
            if z == self.height and (x, y, z-1) in stack:
                return False
        return True

    def drop(self):
        self.cubes = [(x, y, z-1) for x, y, z in self.cubes]
        self.height -= 1

    def canDisintegrate(self, bricks):
        stack = []
        others = [brick for brick in bricks if brick != self]

        for brick in others:
            stack = stack + brick.cubes
        for brick in others:
            if brick.canDrop(stack):
                return False
        return True

def parse(data):
    bricks = []
    for line in data.strip().split('\n'):
        bricks.append(Brick(line))
    return bricks

data = open('data', 'r').read()
bricks = parse(data)

def settle(bricks):
    dropped = set()
    while True:
        stack = []
        for brick in bricks:
            stack = stack + brick.cubes

        drop = []
        for brick in bricks:
            if brick.canDrop(stack):
                drop.append(brick)

        print(f"drop {len(drop)}/{len(bricks)}", )

        if not drop:
            break

        for brick in drop:
            brick.drop()
            dropped.add(brick)
    return len(dropped)

settle(bricks)
disintegrate = []
for brick in bricks:
    if not brick.canDisintegrate(bricks):
        disintegrate.append(brick)

print(disintegrate)
print(len(disintegrate))

total = 0
for brick in disintegrate:
    alt = [x.copy() for x in bricks if x != brick]
    dropped = settle(alt)
    print(f"dropped = {dropped}")
    total += dropped
print(f"total dropped = {total}")
