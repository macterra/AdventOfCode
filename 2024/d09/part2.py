# https://adventofcode.com/2024/day/9

input = "2333133121414131402"
input = open('data', 'r').read()

def parseInput(input):
    vals = [int(x) for x in input if x != '\n']
    memory = []
    lengths = []
    starts = []
    id = 0
    for i in range(len(vals)):
        if i%2 == 0:
            lengths.append(vals[i])
            starts.append(len(memory))
            for j in range(vals[i]):
                memory.append(id)
            id += 1
        else:
            for j in range(vals[i]):
                memory.append(-1)
    return {
        "memory": memory,
        "starts": starts,
        "lengths": lengths
    }

def printDisk(disk):
    for x in disk["memory"]:
        if x < 0:
            print('.', end='')
        else:
            print(x, end='')
    print()

def compactDisk(disk):
    memory = disk["memory"]
    starts = disk["starts"]
    lengths = disk["lengths"]

    for i in range(len(lengths)-1, 0, -1):
        print(i)
        #print(i, lengths[i], starts[i])
        newstart = findSpace(memory, lengths[i])
        if newstart >= 0 and newstart < starts[i]:
            moveFile(memory, starts[i], lengths[i], newstart)
            #printDisk(disk)

def findSpace(memory, length):
    count = 0
    for i in range(len(memory)):
        if memory[i] == -1:
            count += 1
            if count == length:
                return i - length + 1  # Starting index of the free space
        else:
            count = 0
    return -1  # No suitable space found

def moveFile(memory, start, length, newstart):
    # Move file data from current start to new start
    for i in range(length):
        memory[newstart + i] = memory[start + i]
        memory[start + i] = -1  # Clear the old position

disk = parseInput(input)
compactDisk(disk)

checksum = 0
memory = disk["memory"]
for i in range(len(memory)):
    if memory[i] < 0:
        continue
    checksum += i * memory[i]
print(checksum)
