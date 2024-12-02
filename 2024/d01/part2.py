# https://adventofcode.com/2024/day/1

lines = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

f = open('data', 'r')
lines = f.read()

list1 = []
list2 = []

for line in lines.split('\n'):
    if not line:
        continue
    a, b = line.split('   ')
    list1.append(int(a))
    list2.append(int(b))

sim = 0
for i in list1:
    n = 0
    for j in list2:
        if i == j:
            n += 1
    sim += i * n

print(sim)
