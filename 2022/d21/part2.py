data = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

class Monkey:
    def __init__(self, line):
        name, spec = line.split(': ')
        self.name = name
        self.spec = spec

    def yell(self, monkeys):
        if len(self.spec) == 11:
            m1, op, m2 = self.spec.split(' ')

            r1 = monkeys[m1].yell(monkeys)
            r2 = monkeys[m2].yell(monkeys)
            
            if op == '+':
                return r1 + r2
            elif op == '-':
                return r1 - r2
            elif op == '*':
                return r1 * r2
            elif op == '/':
                return r1 / r2
            else:
                exit()

        return int(self.spec)

class Human:
    def __init__(self):
        self.val = 0

    def yell(self, _):
        return self.val
        
def parse(lines):
    monkeys = {}
    for line in lines:
        monkey = Monkey(line)
        monkeys[monkey.name] = monkey
    return monkeys

data = open('data', 'r').read()
lines = data.split('\n')
monkeys = parse(lines)
human = Human()
monkeys['humn'] = human

m1, op, m2 = monkeys['root'].spec.split(' ')
print(m1, m2)

i = 0
base = 0

while True:
    i += 1
    human.val = int(i*1e9)
    y1 = monkeys[m1].yell(monkeys)
    y2 = monkeys[m2].yell(monkeys)
    print(i, y1, y2, y1-y2, y1 == y2)
    if y1 < y2:
        base = int((i-1)*1e9)
        break

print(base)

i = 0
while True:
    i += 1
    human.val = int(i*1e6) + base
    y1 = monkeys[m1].yell(monkeys)
    y2 = monkeys[m2].yell(monkeys)
    print(i, y1, y2, y1-y2, y1 == y2)
    if y1 < y2:
        base += int((i-1)*1e6)
        break

print(base)

i = 0
while True:
    i += 1
    human.val = int(i*1e3) + base
    y1 = monkeys[m1].yell(monkeys)
    y2 = monkeys[m2].yell(monkeys)
    print(i, y1, y2, y1-y2, y1 == y2)
    if y1 < y2:
        base += int((i-1)*1e3)
        break

print(base)

i = 0
while True:
    i += 1
    human.val = i + base
    y1 = monkeys[m1].yell(monkeys)
    y2 = monkeys[m2].yell(monkeys)
    print(i, y1, y2, y1-y2, y1 == y2)
    if y1 == y2:
        base += i
        break

print(base)

human.val = base
y1 = monkeys[m1].yell(monkeys)
y2 = monkeys[m2].yell(monkeys)
print(base, y1, y2, y1-y2, y1 == y2)
