# https://adventofcode.com/2024/day/19

from functools import lru_cache

input = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

def parseInput(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    towels = lines[0].split(', ')
    patterns = lines[1:]
    return towels, patterns

input = open('data', 'r').read()
towels, patterns = parseInput(input)
print(towels, patterns)

@lru_cache(None)
def possiblePatterns(pattern):
    if not pattern:
        return 1
    total = 0
    for towel in towels:
        n = len(towel)
        if towel == pattern[:n]:
            total += possiblePatterns(pattern[n:])
    return total

total = 0
for pattern in patterns:
    count = possiblePatterns(pattern)
    print(f"{pattern} {count}")
    total += count
print(total)
