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

def touching(cube, cubes):
    x, y, z = cube
    touching = 0
    for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        if (x+dx, y+dy, z+dz) in cubes:
            touching += 1
    return touching

def floodFill(cubes):

    x1 = min([ x for x, y, z in cubes ])
    y1 = min([ y for x, y, z in cubes ])
    z1 = min([ z for x, y, z in cubes ])

    x2 = max([ x for x, y, z in cubes ])
    y2 = max([ y for x, y, z in cubes ])
    z2 = max([ z for x, y, z in cubes ])
    
    x, y, z = x1-1, y1-1, z1-1
    queue = [(x, y, z)]
    visited = set()
    flood = set()

    while queue:
        x, y, z = queue.pop(0)

        if (x, y, z) not in visited:
            visited.add((x, y, z))

            if (x, y, z) not in cubes:
                flood.add((x, y, z))

                if x >= x1:
                    queue.append((x-1, y, z))
                if x <= x2:
                    queue.append((x+1, y, z))

                if y >= y1:
                    queue.append((x, y-1, z))
                if y <= y2:
                    queue.append((x, y+1, z))

                if z >= z1:
                    queue.append((x, y, z-1))
                if z <= z2:
                    queue.append((x, y, z+1))
    return flood

print(sum([ touching(c, cubes) for c in floodFill(cubes) ]))
