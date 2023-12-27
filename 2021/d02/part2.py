lines = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

lines = open('data', 'r').read()

lines = lines.split('\n')

x = 0
y = 0
aim = 0

for line in lines:
    cmd, val = line.split(" ")
    val = int(val)
    print(cmd, val)
    if cmd == 'forward':
        x += val
        y += aim * val
    elif cmd == 'down':
        aim += val
    elif cmd == 'up':
        aim -= val
    print(x, y)
print(x*y)