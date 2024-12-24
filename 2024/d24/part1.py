# https://adventofcode.com/2024/day/24

import re

input = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""

input = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
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

        return self.updated

def parseInput(input):
    wiredata, gatedata = input.split('\n\n')

    wires = {}
    gates = {}

    for line in [line for line in wiredata.split('\n') if line.strip() != '']:
        print(line)
        name, val = line.split(': ')
        wires[name] = int(val)

    pattern = r"([a-z]+\d*)\s+(AND|OR|XOR)\s+([a-z]+\d*)\s+->\s+([a-z]+\d*)"
    for line in [line for line in gatedata.split('\n') if line.strip() != '']:
        print(line)
        match = re.match(pattern, line)
        input1 = match.group(1)
        op = match.group(2)
        input2 = match.group(3)
        output = match.group(4)
        print(input1, input2, op, output)
        gates[output] = Gate(op, input1, input2, output)

    return wires, gates

input = open('data', 'r').read()
wires, gates = parseInput(input)

print(wires)
for name in gates:
    print(gates[name])

done = False
while not done:
    done = True
    for _, gate in gates.items():
        if not gate.updated:
            if gate.update(wires):
                done = False
    print(len(wires))

print(wires)

for name in sorted(wires.keys()):
    print(f"{name} {wires[name]}")

result = [(name, val) for name, val in wires.items() if name[0] == 'z']
print(result)
sorted_result = reversed(sorted(result, key=lambda x: x[0]))
all_zs = ''.join(str(val) for _, val in sorted_result)

print(all_zs)
print(int(all_zs, 2))
