# https://adventofcode.com/2024/day/11

input = "125 17"
input = open('data', 'r').read()

cache = {}

def countStones(num, blinks):
    if num in cache and blinks in cache[num]:
        return cache[num][blinks]

    if blinks == 0:
        stones = 1
    elif num == 0:
        stones = countStones(1, blinks-1)
    else:
        s = str(num)
        l = len(s)

        if l%2 == 0:
            stones = countStones(int(s[:l//2]), blinks-1) + countStones(int(s[l//2:]), blinks-1)
        else:
            stones = countStones(num * 2024, blinks-1)

    if not num in cache:
        cache[num] = {}
    cache[num][blinks] = stones
    return stones

stones = [int(x) for x in input.split(' ')]
print(stones)
counts = [countStones(num, 75) for num in stones]
print(counts)
print(sum(counts))
