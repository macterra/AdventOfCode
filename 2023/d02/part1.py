# https://adventofcode.com/2023/day/2

lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

f = open('data', 'r')
lines = f.read()

def parse(line):
    gmax = { 'red': 0, 'green': 0, 'blue': 0 }
    game, draws = line.split(':')
    print(game)
    print(draws)
    for draw in draws.split(';'):
        print(draw)
        for cubes in draw.split(','):
            print(cubes.strip())
            num, color = cubes.strip().split(' ')
            print(f"{num} of {color}")
            gmax[color] = max(int(num), gmax[color])
    return gmax

g = 0
sum = 0
for line in lines.split('\n'):
    if not line:
        continue
    g += 1
    print(line)
    gmax = parse(line)
    print(gmax)
    if gmax['red'] > 12:
        continue
    if gmax['green'] > 13:
        continue
    if gmax['blue'] > 14:
        continue
    sum += g
    print(sum)

print(sum)
