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

def exZone(y, sensors):
    zone = {}
    for sensor in sensors:
        # print(sensor)
        s, b = sensor
        x1, y1 = s
        x2, y2 = b
        hd = abs(x1-x2) + abs(y1-y2)
        vd = abs(y - y1)
        # print(x1, y1, x2, y2, hd, vd)
        if vd <= hd:
            x = x1 + vd - hd
            n = (hd-vd)*2+1
            for i in range(n):
                zone[x] = 1                
                x += 1

    for sensor in sensors:
        s, b = sensor
        x1, y1 = s
        x2, y2 = b
        if y == y1 and x1 in zone:
            del zone[x1]
        if y == y2 and x2 in zone:
            del zone[x2]

    return zone

data = open('data', 'r').read()
lines = data.split('\n')
sensors = parse(lines)
zone = exZone(2000000, sensors)
#print(zone)
print(len(zone))
