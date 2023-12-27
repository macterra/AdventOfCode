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

data = open('data', 'r').read()
lines = data.split('\n')
n = int((len(lines)+1)/7)

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
        return "{}: {} {}".format(self.name, self.items, self.inspections)

    def inspect(self, monkeys):
        for old in self.items:
            new = eval(self.operation)
            new = int(new/3)
            if new % self.test == 0:
                monkeys[self.next].items.append(new)
            else:
                monkeys[self.alt].items.append(new)
            self.inspections += 1
        self.items = []

monkeys = []
for i in range(0,len(lines),7):
    monkey = Monkey(lines[i:i+7])
    monkeys.append(monkey)

for round in range(20):
    for monkey in monkeys:
        monkey.inspect(monkeys)

monkeys.sort(key=lambda x:x.inspections)
monkeys.reverse()
#print(monkeys)

mb = monkeys[0].inspections * monkeys[1].inspections
print(mb)
