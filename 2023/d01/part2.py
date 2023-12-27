# https://adventofcode.com/2023/day/1

lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

f = open('data', 'r')
lines = f.read()

numbers = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

def findFirst(line):
    for i in range(0, len(line)):
        if line[i].isdigit():
            return line[i]
        for j in range(1, 10):
            number = numbers[j-1]
            l = len(number)
            bit = line[i:i+l]
            if bit == number:
                return str(j)

def findLast(line):
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return line[i]
        for j in range(1, 10):
            number = numbers[j-1]
            l = len(number)
            bit = line[i:i+l]
            if bit == number:
                return str(j)

sum = 0
for line in lines.split('\n'):
    if not line:
        continue
    print(line)
    bar = findFirst(line) + findLast(line)
    print(bar)
    sum += int(bar)

print(sum)
