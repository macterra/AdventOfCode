import numpy as np
import re 

input = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682"""

input = open('data', 'r').read()

class Cuboid:
    def __init__(self, on, extent):
        self.on = on
        self.extent = extent

    def __repr__(self):
        return f"[[{'on'if self.on else 'off'} {self.extent}]]"

def makeProc(input):
    lines = input.split('\n')
    cuboids = []
    for line in lines:
        #print(line)
        m = re.match("[onf]+ x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", line)
        #print(m)
        if m:
            on = line[1] == 'n'
            extent = [int(x) for x in m.groups()]
            cuboid = Cuboid(on, extent)
            cuboids.append(cuboid)
        else:
            print(f"failed to parse {line}")
    return cuboids

grid = np.full((101, 101, 101), 0)
print(grid)

cuboids = makeProc(input)
for cuboid in cuboids:
    print(cuboid)
    if min(cuboid.extent) >= -50 and max(cuboid.extent) <= 50:
        x1, x2, y1, y2, z1, z2 = cuboid.extent
        grid[x1+50:x2+51,y1+50:y2+51,z1+50:z2+51] = 1 if cuboid.on else 0

print(len(grid[grid==1]))
