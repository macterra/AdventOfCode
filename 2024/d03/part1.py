# https://adventofcode.com/2024/day/3

import re

data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

f = open('data', 'r')
data = f.read()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.finditer(pattern, data)

sum = 0
for match in matches:
    print(match, match.group(1), match.group(2))
    a = int(match.group(1))
    b = int(match.group(2))
    sum += a*b
print(sum)
