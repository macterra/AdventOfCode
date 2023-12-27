data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

data = open('data', 'r').read()
lines = data.split('\n')

def overlap(a, b, c, d):
    print(a, b, c, d)
    return not(b<c or d<a)

over = 0
for line in lines:
    r1, r2 = line.split(',')
    a, b = r1.split('-')
    c, d = r2.split('-')
    if overlap(int(a), int(b), int(c), int(d)):
        over += 1

print(over)
