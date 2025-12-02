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
while True:
    id = int(str(num) + str(num))
    if id > upperBound:
        break
    #print(id)
    for start, end in rangeList:
        if start <= id <= end:
            print("Invalid ID found:", id)
            sum += id
            break
    num += 1

print("Sum of all invalid IDs:", sum)
