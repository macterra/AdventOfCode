import binascii

test1 = "D2FE28"
test2 = "38006F45291200"
test3 = "EE00D40C823060"
test4 = "8A004A801A8002F478"
test5 = "620080001611562C8802118E34"
test6 = "C0015000016115A2E0802F182340"
test7 = "A0016C880162017C3686B18A3D4780"

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

    def readPacketsLen(self):
        length = self.read(15)
        #print(f"readPacketsLen {length}")
        bits = self.bits[:length]
        self.bits = self.bits[length:]
        while len(bits):
            sub = Packet(bits)
            print(f"sub {sub}")
            bits = sub.bits
            self.versum += sub.versum
        
    def readPacketsNum(self):
        num = self.read(11)
        #print(f"readPacketsNum {num}")
        for i in range(num):
            sub = Packet(self.bits)
            print(f"sub {sub}")
            self.bits = sub.bits
            self.versum += sub.versum

def parsePacket(input):
    bits = hex2bin(input)
    print(bits)
    p = Packet(bits)
    print(p)

parsePacket(input)
