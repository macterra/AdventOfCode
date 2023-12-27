lines = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

f = open('data', 'r')
lines = f.read()

lines = lines.split('\n')

x = 0
y = 0

for line in lines:
    cmd, val = line.split(" ")
    val = int(val)
    print(cmd, val)
    if cmd == 'forward':
        x += val
    elif cmd == 'down':
        y += val
    elif cmd == 'up':
        y -= val
    print(x, y)
print(x*y)