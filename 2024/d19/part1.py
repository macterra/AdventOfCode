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
def patternPossible(pattern):
    if not pattern:
        return True
    for towel in towels:
        n = len(towel)
        if towel == pattern[:n] and patternPossible(pattern[n:]):
            return True
    return False

total = 0
for pattern in patterns:
    if patternPossible(pattern):
        print(f"{pattern} possible")
        total += 1
    else:
        print(f"{pattern} impossible")
print(total)
