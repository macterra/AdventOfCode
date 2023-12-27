# https://adventofcode.com/2023/day/5

input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

input = open('data', 'r').read()

def parseSeeds(section):
    _, seeds = section.split(': ')
    seeds = [int(seed) for seed in seeds.split(' ')]
    return seeds

def parseMap(section):
    ranges = []
    for line in section.split('\n')[1:]:
        nums = [int(num) for num in line.split(' ')]
        ranges.append(nums)
    return ranges

def parse(input):
    sections = input[:-1].split('\n\n')

    return {
        "seeds": parseSeeds(sections[0]),
        "soil": parseMap(sections[1]),
        "fertilizer": parseMap(sections[2]),
        "water": parseMap(sections[3]),
        "light": parseMap(sections[4]),
        "temperature": parseMap(sections[5]),
        "humidity": parseMap(sections[6]),
        "location": parseMap(sections[7]),
    }

def getMapping(val, segments):
    for segment in segments:
        x, y, n = segment
        if val in range(y, y+n):
            return val + x - y
    return val

def findLocation(seed, maps):
    soil = getMapping(seed, maps["soil"])
    fertilizer = getMapping(soil, maps["fertilizer"])
    water = getMapping(fertilizer, maps["water"])
    light = getMapping(water, maps["light"])
    temperature = getMapping(light, maps["temperature"])
    humidity = getMapping(temperature, maps["humidity"])
    location = getMapping(humidity, maps["location"])
    return location

maps = parse(input)
print(maps)

locations = [findLocation(seed, maps) for seed in maps["seeds"]]

print(locations)
print(min(locations))
