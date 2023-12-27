# https://adventofcode.com/2023/day/15

data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
data = open('data', 'r').read()

def hash(token):
    h = 0
    for c in token:
        h += ord(c)
        h *= 17
        h %= 256
    return h

def parse(data):
    instr = []
    tokens = data.strip().split(',')
    for token in tokens:
        if token[-1] == '-':
            label = token[:-1]
            instr.append((label, hash(label), -1))
        else:
            label, focal = token.split('=')
            instr.append((label, hash(label), int(focal)))
    return instr

instructions = parse(data)
print(instructions)
boxes = [[] for _ in range(256)]

for instruction in instructions:
    print(instruction)
    label, h, focal = instruction
    box = boxes[h]
    if focal < 0:
        for i in range(len(box)):
            x, y, z = box[i]
            if x == label:
                del box[i]
                break
    else:
        replaced = False
        for i in range(len(box)):
            x, y, z = box[i]
            if x == label:
                box[i] = instruction
                replaced = True
                break
        if not replaced:
            box.append(instruction)

power = 0
for i in range(len(boxes)):
    box = boxes[i]
    for j in range(len(box)):
        x, y, z = box[j]
        power += (i+1) * (j+1) * z
print(power)
