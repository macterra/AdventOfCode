# https://adventofcode.com/2023/day/1

lines = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

f = open('data', 'r')
lines = f.read()

sum = 0
for line in lines.split('\n'):
    if not line:
        continue
    print(line)
    foo = ''.join(c for c in line if c.isdigit())
    print(foo)
    bar = foo[0] + foo[::-1][0]
    print(bar, int(bar))
    sum += int(bar)

print(sum)
