# https://adventofcode.com/2023/day/24

data = r"""
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

def parse(data):
    stones = []
    for line in data.strip().split('\n'):
        loc, vel = line.split(' @ ')
        x, y, z = [int(val) for val in loc.split(', ')]
        dx, dy, dz = [int(val) for val in vel.split(', ')]
        stones.append(((x, y), (dx, dy)))
    return stones

def intersect(s1, s2):
    print(s1)
    print(s2)
    (x1, y1), (vx1, vy1) = s1
    (x2, y2), (vx2, vy2) = s2

    if vx1 * vy2 == vy1 * vx2:
        # parallel paths
        return None

    t1 = ((x2 - x1) * vy2 - (y2 - y1) * vx2) / (vx1 * vy2 - vy1 * vx2)
    t2 = ((x1 - x2) * vy1 - (y1 - y2) * vx1) / (vx2 * vy1 - vy2 * vx1)

    #print(f"t1={t1:.2f} t2={t2:.2f}")

    if t1 > 0 and t2 > 0:
        intersection_point = (x1 + t1*vx1, y1 + t1*vy1)
        return intersection_point
    else:
        # crossed in the past
        return None


def test(testMin, testMax):
    n = len(stones)
    inside = 0
    for i in range(n-1):
        for j in range(i+1, n):
            cross = intersect(stones[i], stones[j])
            if cross:
                x, y = cross
                within = (x >= testMin) and (y >= testMin) and (x <= testMax) and (y <= testMax)
                print(i, j, f"{x:.2f},{y:.2f} within={within}")
                if within:
                    inside += 1
            else:
                print("no crossing", i, j)
            print()
    return inside

data = open('data', 'r').read()
stones = parse(data)
#print(test(7, 27))
print(test(200000000000000, 400000000000000))
