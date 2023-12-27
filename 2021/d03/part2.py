lines = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

lines = open('data', 'r').read()
lines = lines.split('\n')

print(lines)
width = len(lines[0])
save = lines.copy()

for i in range(width):
    print(lines)
    sum = 0
    num = len(lines)
    if num == 1:
        break
    for j in range(num):
        val = int(lines[j][i])
        sum += val
        #print(i, j, val, sum)
    print(i, num, sum)
    if sum >= num/2:
        match = '1'
    else:
        match = '0'
    next = []
    for j in range(num):
        if lines[j][i] == match:
            next.append(lines[j])
    lines = next

print(lines)
generator = int("".join(lines[0]), 2)
print(generator)

lines = save

for i in range(width):
    print(lines)
    sum = 0
    num = len(lines)
    if num == 1:
        break
    for j in range(num):
        val = int(lines[j][i])
        sum += val
        #print(i, j, val, sum)
    print(i, num, sum)
    if sum >= num/2:
        match = '0'
    else:
        match = '1'
    next = []
    for j in range(num):
        if lines[j][i] == match:
            next.append(lines[j])
    lines = next

print(lines)
scrubber = int("".join(lines[0]), 2)
print(scrubber)

print(generator * scrubber)
