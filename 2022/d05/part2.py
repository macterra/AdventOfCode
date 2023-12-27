import re

data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def parseStacks(lines):
    lines.reverse()
    n = len(lines[0].split('   '))
    stacks = [[] for x in range(n)]
    for line in lines[1:]:
        i = 1
        stack = 0
        while i < len(line):
            crate = line[i]
            if crate != ' ':
                stacks[stack].append(crate)
            i += 4
            stack += 1
    return stacks

def parseMoves(lines):
    moves = []
    for line in lines:
        match = re.search('move (\d+) from (\d+) to (\d+)', line)
        if match:
            a = int(match.group(1))
            b = int(match.group(2))
            c = int(match.group(3))
            moves.append((a,b,c))
    return moves

def parseData(lines):
    i = 0
    while lines[i]:
        i += 1
    stacks = parseStacks(lines[:i])
    moves = parseMoves(lines[i+1:])
    return stacks, moves

data = open('data', 'r').read()
lines = data.split('\n')
stacks, moves = parseData(lines)

print(stacks)

for move in moves:
    a, b, c = move
    print(a, b, c)
    crates = []
    for i in range(a):
        crates.append(stacks[b-1].pop())
    crates.reverse()
    stacks[c-1].extend(crates)
    print(stacks)

top = [stack[-1] for stack in stacks]  
print("".join(top))
