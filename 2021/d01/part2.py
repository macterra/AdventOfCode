
lines = """199
200
208
210
200
207
240
269
260
263"""

#lines = lines.split('\n')

f = open('data', 'r')
lines = f.read().split('\n')

depths = [int(line) for line in lines]
print(depths)

inc = 0
for i in range(1, len(depths)-1):
    a = depths[i-2] + depths[i-1] + depths[i]
    b = depths[i-1] + depths[i] + depths[i+1]
    if b > a:
        inc += 1
print(inc)
