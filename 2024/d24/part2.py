# https://adventofcode.com/2024/day/24

import re
import random
import copy

input = """
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
"""
class Gate:
    def __init__(self, op, input1, input2, output):
        self.op = op
        self.input1 = input1
        self.input2 = input2
        self.output = output
        self.updated = False

    def __str__(self):
        return f"{self.input1} {self.op} {self.input2} -> {self.output}"

    def update(self, wires):
        if not self.updated and self.input1 in wires and self.input2 in wires:
            a = wires[self.input1]
            b = wires[self.input2]

            if self.op == 'AND':
                wires[self.output] = 1 if a and b else 0
            elif self.op == 'OR':
                wires[self.output] = 1 if a or b else 0
            else:
                wires[self.output] = 1 if a != b else 0
            self.updated = True

            # if self.output[0] == 'z':
            #     print(f"{self.output} to {wires[self.output]}")
        return self.updated

def parseInput(input):
    wiredata, gatedata = input.split('\n\n')

    wires = {}
    gates = []

    for line in [line for line in wiredata.split('\n') if line.strip() != '']:
        name, val = line.split(': ')
        wires[name] = int(val)

    pattern = r"([a-z]+\d*)\s+(AND|OR|XOR)\s+([a-z]+\d*)\s+->\s+([a-z]+\d*)"
    for line in [line for line in gatedata.split('\n') if line.strip() != '']:
        match = re.match(pattern, line)
        input1 = match.group(1)
        op = match.group(2)
        input2 = match.group(3)
        output = match.group(4)
        gates.append(Gate(op, input1, input2, output))

    return wires, gates

def run(wires, gates):
    for gate in gates:
        gate.updated = False

    numwires = len(wires)
    while True:
        #print(numwires)
        for gate in gates:
            if not gate.updated:
                gate.update(wires)
        if len(wires) == numwires:
            break
        numwires = len(wires)

    # for gate in gates:
    #     if gate.output[0] == 'z' and not gate.output in wires:
    #         print(f"{gate.output} missing!!!! {gate.updated}")

    result = [(name, val) for name, val in wires.items() if name[0] == 'z']
    sorted_result = reversed(sorted(result, key=lambda x: x[0]))
    all_zs = ''.join(str(val) for _, val in sorted_result)
    return all_zs

def genRandom(n):
    return ''.join(random.choice('01') for _ in range(n))

def testAdd(gates, bits):
    x = genRandom(bits)
    y = genRandom(bits)
    z = int(x, 2) & int(y, 2)
    z = format(z, f"0{bits+1}b")

    wires = {}
    for i in range(bits):
        wires[f"x{str(i).zfill(2)}"] = int(x[bits-i-1])
    for i in range(bits):
        wires[f"y{str(i).zfill(2)}"] = int(y[bits-i-1])

    res = run(wires, gates)

    score = 0
    if len(res) == len(z):
        for i in range(len(z)):
            if res[i] == z[i]:
                score += 1
    score = score/(bits+1)
    return score * score

def testSwap(gates, pairs):
    #print(f"testSwap {pairs}")
    testGates = copy.deepcopy(gates)
    for i in range(0, len(pairs), 2):
        a, b = pairs[i], pairs[i+1]
        testGates[a].output, testGates[b].output = testGates[b].output, testGates[a].output

    score = sum([testAdd(testGates, bits) for _ in range(10)])
    perfect = 10;

    if score == perfect:
        print(f"solution found: {pairs}")
        for i in pairs:
            print(gates[i].output)
        exit(0)

    # for gate in testGates:
    #     print(gate)
    # print(pairs, score)
    return score

input = open('data', 'r').read()
wires, gates = parseInput(input)
bits = len(wires.items())//2
# res = run(wires, gates)
# print(res, len(res))

# print(bits)
# score = testAdd(gates, bits)
# print(score)

n = len(gates)

def calcFitness(population):
    scores = []
    for p in population:
        score = testSwap(gates, p)
        #print(p, score)
        scores.append((p, score))
    return scores

def pickRandom(pool):
    x = random.random()
    sum = 0
    for foo, fit in pool:
        sum += fit
        if sum > x:
            return foo
    return foo

def mutate(a):
    i = random.randint(0, len(a) - 1)
    new_number = random.choice([x for x in range(n) if x not in a])
    mutant = a.copy()
    mutant[i] = new_number
    return mutant

def crossover(a, b):
    if a == b:
        return mutate(a)

    s = random.randint(0, len(a)-1)
    return a[:s] + b[s:]

def genetic(scores):
    sz = len(scores)
    fitness = sorted(scores, key=lambda item: item[1])
    best = fitness[-1]
    print(f"best = {best}")
    total = sum([score for _, score in scores]) or 1
    #print(fitness, total)
    normed = [(foo, score/total) for foo, score in scores]
    #print(normed)
    pool = sorted(normed, key=lambda item: item[1])
    #print(pool)
    next = [ best[0] ]
    for _ in range(sz-1):
        a = pickRandom(pool)
        b = pickRandom(pool)
        c = crossover(a, b)
        #print(c)
        next.append(c)
        #print(a, b, c)
    return next

population = [random.sample(range(n), 8) for _ in range(4000)]
gen = 1
while True:
    print(gen)
    fitness = calcFitness(population)
    population = genetic(fitness)
    gen += 1
