# https://adventofcode.com/2024/day/9

input = "2333133121414131402"
input = open('data', 'r').read()

def parseInput(input):
    vals = [int(x) for x in input if x != '\n']
    disk = []
    id = 0
    for i in range(len(vals)):
        if i%2 == 0:
            for j in range(vals[i]):
                disk.append(id)
            id += 1
        else:
            for j in range(vals[i]):
                disk.append(-1)
    return disk

def compactDisk(disk):
    p1 = 0
    p2 = len(disk)-1

    while True:
        while disk[p1] >= 0:
            p1 += 1
        while disk[p2] < 0:
            p2 -= 1
        if p2 <= p1:
            break
        disk[p1] = disk[p2]
        disk[p2] = -1
        #print(disk)

disk = parseInput(input)
compactDisk(disk)

checksum = 0
for i in range(len(disk)):
    if disk[i] < 0:
        break
    checksum += i * disk[i]
print(checksum)
