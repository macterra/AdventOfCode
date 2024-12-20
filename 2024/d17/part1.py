# https://adventofcode.com/2024/day/17

input = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
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

    def run(self):
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
        print(f"{self.combo(op)%8},", end='')

input = open('data', 'r').read()
computer = Computer(input)
computer.run()
print()
