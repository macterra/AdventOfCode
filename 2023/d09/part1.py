# https://adventofcode.com/2023/day/9

data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

def parse(data):
    lines = data.strip().split('\n')
    readings = []
    for line in lines:
        readings.append([int(x) for x in line.split(' ')])
    return readings

def predict(reading):
    reduced = [reading[i] - reading[i-1] for i in range(1, len(reading))]
    print(reduced)
    if all(x == 0 for x in reduced):
        return reading[-1]
    else:
        return reading[-1] + predict(reduced)

data = open('data', 'r').read()

readings = parse(data)
print(readings)

predictions = [predict(reading) for reading in readings]
print(predictions)
print(sum(predictions))
