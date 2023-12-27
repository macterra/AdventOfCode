import math

data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

class Monkey:
    def __init__(self, lines):
        self.name = lines[0][:-1]
        self.items = [int(x) for x in lines[1][18:].split(',')]
        self.operation = lines[2][19:]
        self.test = int(lines[3][21:])
        self.next = int(lines[4][29:])
        self.alt = int(lines[5][30:])
        self.inspections = 0

    def __repr__(self) -> str:
        return "{} inspected items {} times. {}".format(self.name, self.inspections, self.items)

    def inspect(self, monkeys, cycle):
        for old in self.items:
            new = eval(self.operation) % cycle

            if new % self.test == 0:
                monkeys[self.next].items.append(new)
            else:
                monkeys[self.alt].items.append(new)
            self.inspections += 1
        self.items = []

data = open('data', 'r').read()
lines = data.split('\n')
n = int((len(lines)+1)/7)

monkeys = []
for i in range(0,len(lines),7):
    monkey = Monkey(lines[i:i+7])
    monkeys.append(monkey)

cycle = math.prod([monkey.test for monkey in monkeys])
print(cycle)

for round in range(1, 10001):
    for monkey in monkeys:
        monkey.inspect(monkeys, cycle)

    if round in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:     
        print("== After round {} ==".format(round))
        for monkey in monkeys:
            print(monkey)
        print()

monkeys.sort(key=lambda x:x.inspections)
monkeys.reverse()

mb = monkeys[0].inspections * monkeys[1].inspections
print(mb)
