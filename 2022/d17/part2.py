
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

def resetRocks():
    global rocks
    global defaultRocks
    rocks = list(defaultRocks)

def nextRock():
    rock = rocks.pop(0)
    rocks.append(rock)
    return shiftRock(rock, 2, 0)

def resetJets():
    global jets
    jets = list(data)

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
rocks.append(makeRock(3,3,"###..#..#"))
rocks.append(makeRock(1,4,"####"))
rocks.append(makeRock(2,2,"####"))
defaultRocks = list(rocks)

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

def findPattern(deltas, test):
    l = len(deltas)
    if l < 2*test:
        return 0
    for j in range(l-2*test):
        if deltas[j:j+test] == deltas[-test:]:
            print(j, test, deltas[j:j+test], deltas[-test:])
            return j
    return 0

def topOfTower(n):
    resetRocks()
    resetJets()    
    chamber = set()
    for _ in range(n):
        dropRock(chamber)
    return findTop(chamber)

def validateCycle(start, base, cycle):
    clen = len(cycle)
    print("validate start={} base={} cycle len={}", start, base, clen)

    resetRocks()
    resetJets()
    chamber = set()
    last = findTop(chamber)
    deltas = []
    tops = []
    for i in range(10000):
        dropRock(chamber)
        top = findTop(chamber)
        delta = top-last
        print(i, last, top, delta)
        deltas.append(delta)
        tops.append(top)
        last = top

        if i >= start:
            print((i-start)%clen)
            assert(delta == cycle[(i-start)%clen])

def part2():
    resetRocks()
    resetJets()
    chamber = set()
    last = findTop(chamber)
    deltas = []
    tops = []
    for i in range(100000):
        dropRock(chamber)
        top = findTop(chamber)
        #print(i, last, top, top-last)
        deltas.append(top-last)
        tops.append(top)
        last = top
        test = 147
        j = findPattern(deltas, test)
        if j > 0:
            break

    print(i, i-test, j)
    print(tops[j], tops[i-test], tops[i-test]-tops[j])
    base = sum(deltas[:j])
    cycle = i-j-test-1
    fullcycle = deltas[j:j+cycle+2]
    cycle = len(fullcycle)
    inc = sum(fullcycle)
    print("j={} base={} cycle={} inc={}".format(j, base, cycle, inc))
    T = 1000000000000
    T -= j            
    print("T={} cycles={} modulo={}".format(T, T//cycle, T%cycle))
    top = base + T//cycle * inc + sum(fullcycle[:T%cycle])
    print(top)

part2()
