# https://adventofcode.com/2023/day/4

lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

f = open('data', 'r')
lines = f.read()

def parse(line):
    card, rest = line.split(':')
    wins, nums = rest.split('|')
    wins = [int(wins[i:i+3]) for i in range(0, len(wins)-1, 3)]
    nums = [int(nums[i:i+3]) for i in range(0, len(nums), 3)]
    return wins, nums

sum = 0
for line in lines.split('\n')[:-1]:
    wins, nums = parse(line)
    hits = set(wins).intersection(set(nums))
    print(wins, nums, hits)
    n = len(hits)
    if n > 0:
        points = 2 ** (n-1)
        sum += points
        print(n, points, sum)

print(sum)
