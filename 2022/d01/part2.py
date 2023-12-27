lines = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

f = open('data', 'r')
lines = f.read()

cals = 0
elves = []

for line in lines.split('\n'):
    if line:
        print(int(line))
        cals += int(line)
    else:
        elves.append(cals)
        cals = 0

elves.append(cals)

elves.sort()
elves.reverse()

print(elves[0] + elves[1] + elves[2])
