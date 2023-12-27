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
print(width)

gamma = []
epsilon = []

for i in range(width):
    sum = 0
    num = len(lines)
    for j in range(num):
        val = int(lines[j][i])
        sum += val
        #print(i, j, val, sum)
    print(i, num, sum)
    if sum > num/2:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gamma = "".join(gamma)
gamma = int(gamma, 2)

epsilon = "".join(epsilon)
epsilon = int(epsilon, 2)

print(gamma, epsilon, gamma*epsilon)
