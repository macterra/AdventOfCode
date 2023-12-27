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
                return int(r1 / r2)
            else:
                exit()

        return int(self.spec)
        
def parse(lines):
    monkeys = {}
    for line in lines:
        monkey = Monkey(line)
        monkeys[monkey.name] = monkey
    return monkeys

data = open('data', 'r').read()
lines = data.split('\n')
monkeys = parse(lines)

print(monkeys['root'].yell(monkeys))
