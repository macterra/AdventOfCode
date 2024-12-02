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

list1.sort()
list2.sort()

print(list1)
print(list2)

sum = 0
for i in range(len(list1)):
    print(i, list1[i], list2[i])
    sum += abs(list2[i] - list1[i])

print(sum)
