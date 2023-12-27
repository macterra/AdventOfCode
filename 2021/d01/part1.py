
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

f = open('data', 'r')
lines = f.read().split('\n')

depths = [int(line) for line in lines]
print(depths)

inc = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        inc += 1
print(inc)
