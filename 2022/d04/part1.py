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
    if b-a > d-c:
        return c >= a and d <= b            
    else:
        return a >= c and b <= d

con = 0
for line in lines:
    #print(line)
    r1, r2 = line.split(',')
    #print(r1, r2)
    a, b = r1.split('-')
    c, d = r2.split('-')
    if overlap(int(a), int(b), int(c), int(d)):
        con += 1
print(con)
