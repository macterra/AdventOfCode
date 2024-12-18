# https://adventofcode.com/2024/day/17

import random

input = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

class Computer:
    def __init__(self, input):
        registers, program = input.split('\n\n')
        lines = [line for line in registers.split('\n') if line.strip() != '']
        _, a = lines[0].split(': ')
        _, b = lines[1].split(': ')
        _, c = lines[2].split(': ')
        self.regA = int(a)
        self.regB = int(b)
        self.regC = int(c)

        lines = [line for line in program.split('\n') if line.strip() != '']
        _, program = lines[0].split(': ')
        self.program = [int(i) for i in program.split(',')]
        self.ip = 0
        self.steps = 0
        self.output = []

    def run(self, regA):
        self.regA = regA
        self.regB = 0
        self.regC = 0
        self.ip = 0
        self.steps = 0
        self.output = []

        while self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip+1]

            #print(self.ip, opcode, operand)

            if opcode == 0:
                self.adv(operand)
            elif opcode == 1:
                self.bxl(operand)
            elif opcode == 2:
                self.bst(operand)
            elif opcode == 3:
                self.jnz(operand)
            elif opcode == 4:
                self.bxc(operand)
            elif opcode == 5:
                self.out(operand)
            elif opcode == 6:
                self.bdv(operand)
            elif opcode == 7:
                self.cdv(operand)

            if opcode != 3:
                self.ip += 2

            self.steps += 1

            # print(self.output)
            # print(self.program[:len(self.output)])
            # print(self.output == self.program[:len(self.output)])
            outlen = len(self.output)
            if self.output != self.program[:outlen]:
                return False
            if outlen > len(self.program):
                return False
        return self.output == self.program

    def combo(self, operand):
        if operand == 4:
            return self.regA
        if operand == 5:
            return self.regB
        if operand == 6:
            return self.regC
        return operand

    def adv(self, op):
        self.regA = self.regA // (2 ** self.combo(op))

    def bdv(self, op):
        self.regB = self.regA // (2 ** self.combo(op))

    def cdv(self, op):
        self.regC = self.regA // (2 ** self.combo(op))

    def bxl(self, op):
        self.regB = self.regB ^ op

    def bst(self, op):
        self.regB = self.combo(op)%8

    def jnz(self, op):
        if self.regA != 0:
            self.ip = op
        else:
            self.ip += 2

    def bxc(self, op):
        self.regB = self.regB ^ self.regC

    def out(self, op):
        #print(f"{self.combo(op)%8},", end='')
        self.output.append(self.combo(op)%8)

input = open('data', 'r').read()
computer = Computer(input)

solutions = []

def calcFitness(population):
    scores = []
    for regA in population:
        if computer.run(regA):
            print(f">>> {regA} {computer.output}")
            solutions.append(regA)
        outlen = len(computer.output)
        score = outlen
        #print(regA, computer.steps, len(computer.output), computer.output, correct, score)
        scores.append((regA, score))
    return scores

def pickRandom(pool):
    x = random.random()
    sum = 0
    for num, fit in pool:
        sum += fit
        if sum > x:
            return num
    return num

def mutate(a):
    return a ^ (1 << random.randint(0, 47))

def crossover(a, b):
    if a == b:
        return mutate(a)

    ba = bin(a)
    bb = bin(b)
    if len(ba) != len(bb):
        return mutate(a)
    else:
        s = random.randint(0, len(ba)-1)
        r = ba[:s] + bb[s:]
        if len(r) != len(ba):
            raise IndexError
        return int(r, 2)

def genetic(scores):
    sz = len(scores)
    fit = { p: s for p, s in scores }
    total = sum(fit.values())
    #print(fit, total)
    normed = {k: v/total for k, v in fit.items()}
    #print(normed)
    pool = sorted(normed.items(), key=lambda item: item[1])
    best = pool[-1][0]
    print(f"best = {best} {fit[best]}")
    next = [ best ]
    for _ in range(sz-1):
        a = pickRandom(pool)
        b = pickRandom(pool)
        c = crossover(a, b)
        next.append(c)
        #print(a, b, c)
    return next

popsize = 8000
population = [random.randint(0, 2**48) for _ in range(popsize)]

gen = 1
while True:
    print(gen)
    fitness = calcFitness(population)
    population = genetic(fitness)
    print(solutions)
    gen += 1
