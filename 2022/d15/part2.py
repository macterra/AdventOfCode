import re

data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

def parse(lines):
    sensors = []
    for line in lines:
        match = re.search("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        if match:
            x1 = match.group(1)
            y1 = match.group(2)
            x2 = match.group(3)
            y2 = match.group(4)
            sensors.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return sensors

def makeRegions(sensors):
    regions = []
    for sensor in sensors:
        # print(sensor)
        s, b = sensor
        x1, y1 = s
        x2, y2 = b
        hd = abs(x1-x2) + abs(y1-y2)
        lcx = x1 - hd
        rcx = x1 + hd
        tcx, tcy = lcx + y1, y1 - lcx # top left corner
        bcx, bcy = rcx + y1, y1 - rcx # bottom right corner
        regions.append(((tcx, tcy), (bcx, bcy)))
        #print(s, b, x1, y1, x2, y2, hd)
        #print(y1, lcx, rcx)
    return regions

def locateGaps(regions):
    n = len(regions)
    xs = set()
    ys = set()
    for i in range(n):
        r1 = regions[i]
        c1, c2 = r1
        x1, y1 = c1
        x2, y2 = c2
        for j in range(n):
            r2 = regions[j]
            #print(i, j, r1, r2)
            c3, c4 = r2
            x3, y3 = c3
            x4, y4 = c4
            dx = x3-x2
            dy = y2-y3
            if dx == 2:
                xs.add(x2+1)
            if dy == 2:
                ys.add(y3+1)
    return xs, ys

def isCovered(x, y, regions):
    for region in regions:
        #print(x, y, region)
        c1, c2 = region
        x1, y1 = c1
        x2, y2 = c2
        #print(x1, x, x2, x1 <= x <= x2)
        #print(y1, y, y2, y1 <= y <= y2)
        if x1 <= x <= x2 and y2 <= y <= y1:
            return False
    return True

data = open('data', 'r').read()
lines = data.split('\n')
sensors = parse(lines)
regions = makeRegions(sensors)
xs, ys = locateGaps(regions)

for x in xs:
    for y in ys:
        found = isCovered(x,y,regions)
        if found:
            x, y = (x-y)>>1, (x+y)>>1
            freq = x * 4000000 + y
            print('found', x, y, freq)
