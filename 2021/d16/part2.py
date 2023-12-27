"""
C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
04005AC33890 finds the product of 6 and 9, resulting in the value 54.
880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
D8005AC2A8F0 produces 1, because 5 is less than 15.
F600BC2D8F produces 0, because 5 is not greater than 15.
9C005AC2F8F0 produces 0, because 5 is not equal to 15.
9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
"""

tests = [
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 15),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1)
]

input = open('data', 'r').read()

def hex2bin(hex):
    bin = []
    for c in hex:
        bin.extend([f'{int(c,16):0>4b}'])
    return "".join(bin)

class Packet:
    def __init__(self, bits):
        self.bits = bits
        self.value = 0
        self.parse()

    def __repr__(self):
        return f"Packet ver={self.version} type={self.type} value={self.value} len={len(self.bits)} versum={self.versum}"

    def read(self, len):
        pop = self.bits[:len]
        self.bits = self.bits[len:]
        return int(pop,2)

    def parse(self):
        self.version = self.read(3)
        self.versum = self.version
        self.type = self.read(3)

        if self.type == 4: # literal
            cont = self.read(1)
            self.value = self.read(4)
            while cont:
                self.value *= 16
                cont = self.read(1)
                self.value += self.read(4)
        else: # operator
            op = self.read(1)
            if op == 0:
                self.readPacketsLen()
            else:
                self.readPacketsNum()

            if self.type == 0: # sum
                self.value = 0
                for sub in self.subs:
                    self.value += sub.value
            elif self.type == 1: # product
                self.value = 1
                for sub in self.subs:
                    self.value *= sub.value
            elif self.type == 2: # min
                self.value = min([sub.value for sub in self.subs])
            elif self.type == 3: # min
                self.value = max([sub.value for sub in self.subs])
            elif self.type == 5: # greater than
                if self.subs[0].value > self.subs[1].value:
                    self.value = 1
                else:
                    self.value =  0
            elif self.type == 6: # less than
                if self.subs[0].value < self.subs[1].value:
                    self.value = 1
                else:
                    self.value =  0
            elif self.type == 7: # equal
                if self.subs[0].value == self.subs[1].value:
                    self.value = 1
                else:
                    self.value =  0

    def readPacketsLen(self):
        length = self.read(15)
        #print(f"readPacketsLen {length}")
        bits = self.bits[:length]
        self.bits = self.bits[length:]
        self.subs = []
        while len(bits):
            sub = Packet(bits)
            #print(f"sub {sub}")
            bits = sub.bits
            self.versum += sub.versum
            self.subs.append(sub)
        
    def readPacketsNum(self):
        num = self.read(11)
        #print(f"readPacketsNum {num}")
        self.subs = []
        for i in range(num):
            sub = Packet(self.bits)
            #print(f"sub {sub}")
            self.bits = sub.bits
            self.versum += sub.versum
            self.subs.append(sub)

def runTests():
    for input, result in tests:
        bits = hex2bin(input)
        print(bits)
        p = Packet(bits)
        print(p)
        print(input, result, p.value == result)

print(Packet(hex2bin(input)))