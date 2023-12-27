input = "target area: x=20..30, y=-10..-5"
input = "target area: x=70..96, y=-179..-124"

def parseInput(input):
    _, areas = input.split(':')
    x, y = areas.split(',')
    _, xrange = x.split('=')
    _, yrange = y.split('=')
    x1, x2 = xrange.split("..")
    y1, y2 = yrange.split("..")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    return x1, x2, y1, y2

x1, x2, y1, y2 = parseInput(input)
print(x1, x2, y1, y2)

def shoot(vx, vy, x1, x2, y1, y2):
    x = 0
    y = 0
    maxy = 0
    hit = False

    while x < x2 and y > y1:
        x += vx
        y += vy

        if vx > 0:
            vx -= 1

        if vx < 0:
            vx += 1            

        vy -= 1

        maxy = max(maxy, y)

        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return maxy

        #print(f"    x={x} y={y} vx={vx} vy={vy} maxy={maxy}")

    return 0


maxy = 0

for vx in range(1, 2000):
    for vy in range(1, 2000):
        y = shoot(vx, vy, x1, x2, y1, y2)
        if y > maxy:
            maxvx = vx
            maxvy = vy
            maxy = y
        print(f"shoot vx= {vx}, vy={vy}, y={y} maxy={maxy}")

print(f"maxvx={maxvx} maxvy={maxvy} maxy={maxy}")