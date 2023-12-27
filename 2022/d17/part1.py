
data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
data = open('data', 'r').read().strip()
jets = list(data)

def makeRock(w, h, pattern):
    rock = []
    for i in range(h):
        for j in range(w):
            if pattern[i*w+j] == '#':
                rock.append((j+1,i+1))
    print(rock)
    return rock

def shiftRock(rock, dx, dy):
    return [(x+dx, y+dy) for x, y in rock]

def collide(rock, chamber):
    for x, y in rock:
        if x < 1:
            return True
        if x > 7:
            return True
        if y < 1:
            return True
        if (x, y) in chamber:
            return True
    return False

def nextRock():
    rock = rocks.pop(0)
    rocks.append(rock)
    return shiftRock(rock, 2, 0)

def nextJet():
    jet = jets.pop(0)
    jets.append(jet)
    return jet

def findTop(chamber):
    if len(chamber) > 0:
        return max([y for x, y in chamber])
    else:
        return 0

def printChamber(chamber):
    top = findTop(chamber)

    for row in range(top, 1, -1):
        print('|', end='')
        for i in range(1, 8):
            if (i, row) in chamber:
                print('#', end='')
            else:
                print('.', end='')
        print('|')
    print('+-------+')

rocks = []
rocks.append(makeRock(4,1,"####"))
rocks.append(makeRock(3,3,".#.###.#."))
rocks.append(makeRock(3,3,"###..#..##"))
rocks.append(makeRock(1,4,"####"))
rocks.append(makeRock(2,2,"####"))

chamber = set()

def dropRock(chamber):
    rock = nextRock()
    top = findTop(chamber)
    rock = shiftRock(rock, 0, top+3)

    while True:
        jet = nextJet()

        if jet == '<':
            shifted = shiftRock(rock, -1, 0)
        else:
            shifted = shiftRock(rock, 1, 0)

        if not collide(shifted, chamber):
            rock = shifted

        drop = shiftRock(rock, 0, -1)

        if collide(drop, chamber):
            break
        else:
            rock = drop

    for chunk in rock:
        chamber.add(chunk)

for i in range(2022):
    dropRock(chamber)

print(findTop(chamber))
