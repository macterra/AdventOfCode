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

# https://adventofcode.com/2023/day/5

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

def applySegment(band, segments):
    print(band, segments)
    a, b = band
    newbands = []

    for x, y, n in segments:
        if (y+n) < a:
            continue

        if b < y:
            break

        if a < y:
            newbands.append((a, y-1))
            a = y

        a2 = min(b, y+n-1)
        x1 = a + x - y
        x2 = a2 + x - y
        newbands.append((x1, x2))
        a = a2 + 1

        if a > b:
            break

    if (a <= b):
        newbands.append((a, b))

    return newbands

def getMapping(bands, segments):
    segments = sorted(segments, key=lambda x: x[1])
    newbands = []
    for band in bands:
        newbands.extend(applySegment(band, segments))
    return newbands

def findLocation(seeds, maps):
    soil = getMapping(seeds, maps["soil"])
    fertilizer = getMapping(soil, maps["fertilizer"])
    water = getMapping(fertilizer, maps["water"])
    light = getMapping(water, maps["light"])
    temperature = getMapping(light, maps["temperature"])
    humidity = getMapping(temperature, maps["humidity"])
    location = getMapping(humidity, maps["location"])
    return location

maps = parse(input)
print(maps)

seeds = maps["seeds"]
seeds = [ (seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
print(seeds)
location = findLocation(seeds, maps)
print(location)
print(min([ a for a, b in location]))

#print(applySegment((100,200), [(10, 10, 10), (0, 90, 40), (300, 120, 10), (400, 200, 20)]))
