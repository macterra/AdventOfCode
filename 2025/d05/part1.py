# https://adventofcode.com/2025/day/5

lines = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

lines = open('data', 'r').read()

ranges, ingredients = lines.strip().split('\n\n')

ranges = ranges.split('\n')
ranges = [tuple(map(int, r.split('-'))) for r in ranges]

ingredients = ingredients.split('\n')
ingredients = [int(i) for i in ingredients]

print("Ranges:", ranges)
print("Ingredients:", ingredients)

fresh = 0
for ingredient in ingredients:
    for a, b in ranges:
        if a <= ingredient <= b:
            fresh += 1
            break

print("Fresh ingredients count:", fresh)
