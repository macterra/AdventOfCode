# https://adventofcode.com/2025/day/2

input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

f = open('data', 'r')
lines = f.read()
input = lines.strip()

ranges = input.split(',')
rangeList = []
for r in ranges:
    start, end = map(int, r.split('-'))
    rangeList.append((start, end))

rangeList.sort()
print(rangeList)
upperBound = rangeList[-1][1]
print("Upper Bound:", upperBound)

num = 1
sum = 0
invalid = {}

while True:
    id = int(str(num) + str(num))
    if id > upperBound:
        break
    while id <= upperBound:
        #print(id)
        for start, end in rangeList:
            if start <= id <= end:
                if id not in invalid:
                    print("Invalid ID found:", id)
                    invalid[id] = True
                    sum += id
                break
        id = int(str(id) + str(num))
    num += 1

print("Sum of all invalid IDs:", sum)
