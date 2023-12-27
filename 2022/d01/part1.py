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

max = 0
cals = 0

for line in lines.split('\n'):
    if line:
        print(int(line))
        cals += int(line)
    else:
        if cals > max:
            max = cals
        cals = 0

print(max)
