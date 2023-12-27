input = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""

class ALU:
    def __init__(self, input):
        prog = []
        lines = input.split('\n')
        for line in lines:
            prog.append(line.split(' '))
        self.prog = prog
        self._reset()

    def _reset(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.valid = False

    def __repr__(self):
        return f"w={self.w} x={self.x} y={self.y} z={self.z} valid={self.valid}"

    def run(self, input):
        self._reset()
        self.input = [x for x in str(input)]

        for p in self.prog:
            self.execute(p)
            #print(self)
        self.valid = self.z == 0
        return self.valid

    def execute(self, p):
        op = p[0]
        reg = p[1]
        #print(f"exec {op} on {reg}")

        if op == 'inp':
            self._inp(reg)
        else:
            b = p[2]
            if b in "wxyz":
                b = self._reg(b)
            else:
                b = int(b)

            if op == 'add':
                self._add(reg, b)
            elif op == 'mul':
                self._mul(reg, b)
            elif op == 'div':
                self._div(reg, b)
            elif op == 'mod':
                self._mod(reg, b)
            elif op == 'eql':
                self._eql(reg, b)              

    def _reg(self, reg):
        if reg == 'w':
            return self.w
        if reg == 'x':
            return self.x
        if reg == 'y':
            return self.y
        if reg == 'z':
            return self.z

    def _inp(self, reg):
        v = int(self.input.pop(0))
        #print(f"inp {v} into {reg}")
        #print(self.input)
        if reg == 'w':
            self.w = v
        elif reg == 'x':
            self.x = v
        elif reg == 'y':
            self.y = v
        elif reg == 'z':
            self.z = v

    def _add(self, reg, b):
        if reg == 'w':
            self.w += b
        elif reg == 'x':
            self.x += b
        elif reg == 'y':
            self.y += b
        elif reg == 'z':
            self.z += b

    def _mul(self, reg, b):
        if reg == 'w':
            self.w *= b
        elif reg == 'x':
            self.x *= b
        elif reg == 'y':
            self.y *= b
        elif reg == 'z':
            self.z *= b

    def _div(self, reg, b):
        if reg == 'w':
            self.w //= b
        elif reg == 'x':
            self.x //= b
        elif reg == 'y':
            self.y //= b
        elif reg == 'z':
            self.z //= b

    def _mod(self, reg, b):
        if reg == 'w':
            self.w %= b
        elif reg == 'x':
            self.x %= b
        elif reg == 'y':
            self.y %= b
        elif reg == 'z':
            self.z %= b

    def _eql(self, reg, b):
        if reg == 'w':
            self.w = 1 if self.w == b else 0
        elif reg == 'x':
            self.x = 1 if self.x == b else 0
        elif reg == 'y':
            self.y = 1 if self.y == b else 0
        elif reg == 'z':
            self.z = 1 if self.z == b else 0

input = open('data', 'r').read()
alu = ALU(input)
print(len(alu.prog))

import random

def randomModelNum():
    x = [str(random.randint(1,9)) for i in range(14)]
    #print(x)
    return "".join(x)

def test1():
    n = 0
    minz = 9999999999
    while True:
        n += 1
        num = randomModelNum()
        print(n, num, minz)
        if alu.run(num):
            break
        minz = min(minz, alu.z)

def pickRandom(pool):
    x = random.random()
    sum = 0
    for num, fit in pool:
        sum += fit
        if sum > x:
            return num
    return num

def mutate(a):
    l = len(a)
    x = random.randint(0, l-1)
    if x > 0:
        c = a[:x-1] + str(random.randint(1,9)) + a[x:]
    else:
        c = str(random.randint(1,9)) + a[1:]
    #print(f"mutated {a} at {x} to {c} {len(c)}")
    return c

def crossover(a, b):
    if a == b:
        return mutate(a)

    l = len(a)
    x = random.randint(0, l-1)
    c = a[:x] + b[x:]
    #print(f"crossover {a} x {b} at {x} = {c} {len(c)}")
    return c

def fitness(k, z):
    if z > 0:
        return 1/(1+z)
    else:
        x = int(k)/1e13
        return x

def genetic(alu, pop):
    z = {}
    for i in pop:
        alu.run(i)
        z[i] = alu.z
    #print(z)
    minz = min(z.values())
    if minz == 0:
        for k in z:
            if z[k] == 0:
                print(f"valid! {k}")
    print(f"min z = {minz}")
    fit = {k:fitness(k,v) for k, v in z.items()}
    total = sum(fit.values())
    #print(fit, total)
    normed = {k: v/total for k, v in fit.items()}
    #print(normed)
    pool = sorted(normed.items(), key=lambda item: item[1])
    sz = len(pop)
    best = pool[-1][0]
    print(f"best = {best} {fit[best]}")
    next = [ best ]
    for i in range(sz-1):
        a = pickRandom(pool)
        b = pickRandom(pool)
        c = crossover(a, b)
        next.append(c)
        #print(a, b, c)
    return next

pop = {randomModelNum() for i in range(10000)}
print(pop)

for i in range(1000):
    pop = genetic(alu, pop)
    #print(pop)
