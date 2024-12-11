# https://adventofcode.com/2024/day/11

input = "125 17"
input = open('data', 'r').read()

def blink(stones):
    next = []
    for stone in stones:
        if stone == 0:
            next.append(1)
        elif len(str(stone))%2 == 0:
            s = str(stone)
            l = len(s)
            next.append(int(s[:l//2]))
            next.append(int(s[l//2:]))
        else:
            next.append(stone * 2024)
    return next

stones = [int(x) for x in input.split(' ')]

for i in range(26):
    print(i, len(stones))
    stones = blink(stones)
