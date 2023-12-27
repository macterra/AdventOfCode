data = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

def parse(lines):
    cubes = {}
    for line in lines:
        pos = [int(x) for x in line.split(',')]
        cubes[tuple(pos)] = 1
    return cubes

data = open('data', 'r').read()
lines = data.split('\n')
cubes = parse(lines)

def exposed(cube, cubes):
    x, y, z = cube

    touching = 0
    for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        if (x+dx, y+dy, z+dz) in cubes:
            touching += 1
    print(cube, touching)
    return 6-touching

faces = 0
for cube in cubes:
    faces += exposed(cube, cubes)

print(faces)
