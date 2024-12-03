# https://adventofcode.com/2024/day/3

import re

data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

f = open('data', 'r')
data = f.read()

do = r"do\(\)"
dont = r"don\'t\(\)"
pattern = r"mul\((\d+),(\d+)\)"

sum = 0
on = True
i = 0
while i < len(data):
    rest = data[i:]
    #print(rest)

    if re.match(do, rest):
        on = True
        i += 4
        print('on')
        continue

    if re.match(dont, rest):
        on = False
        i += 7
        print('off')
        continue

    match = re.match(pattern, rest)
    if match:
        if on:
            a = int(match.group(1))
            b = int(match.group(2))
            sum += a*b
        i += len(match.group(0))
        print(match.group(0))
        continue

    i += 1
print(sum)
