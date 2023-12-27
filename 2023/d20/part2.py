# https://adventofcode.com/2023/day/20

from enum import Enum
from collections import deque
from math import gcd

data = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

data = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

class ModuleType(Enum):
    FLIP_FLOP = "%"
    CONJUCTION = "&"
    BROADCASTER = "broadcaster"

class Module:
    modules = {}
    events = deque()
    outputs = []
    count = 0
    rxTrigger = None
    lengths = {}
    counters = {}

    @classmethod
    def init(cls):
        for name in cls.modules:
            cls.modules[name].connect()
        for name in cls.outputs:
            Module(f"{name} -> ")
        for name in Module.modules:
            if 'rx' in Module.modules[name].outputs:
                cls.rxTrigger = name
        cls.counters = { name: 0 for name, module in cls.modules.items() if cls.rxTrigger in module.outputs }

    @classmethod
    def pushButton(cls):
        cls.count += 1
        cls.events.append(('button', 0, 'broadcaster'))

        while cls.events:
            source, signal, target = cls.events.popleft()
            module = cls.modules[target]

            if module.name == cls.rxTrigger and signal == 1:
                cls.counters[source] += 1

                if source not in cls.lengths:
                    cls.lengths[source] = cls.count

                if all(cls.counters.values()):
                    product = 1
                    for length in cls.lengths.values():
                        product = product * length // gcd(product, length)
                    print(product)
                    exit(0)

            module.pulse(source, signal)

    def __init__(self, spec):
        name, outputs = spec.split(' -> ')

        self.name = name
        self.type = ModuleType.BROADCASTER
        self.state = 0
        self.received = set()

        if name[0] == '&':
            self.type = ModuleType.CONJUCTION
            self.name = name[1:]

        if name[0] == '%':
            self.type = ModuleType.FLIP_FLOP
            self.name = name[1:]

        if outputs:
            self.outputs = outputs.split(', ')
        else:
            self.outputs = []

        self.inputs = {}
        Module.modules[self.name] = self

    def __repr__(self):
        return f"Module {self.name} -> {self.outputs}"

    def connect(self):
        for name in self.outputs:
            if name in Module.modules:
                Module.modules[name].hello(self.name)
            else:
                Module.outputs.append(name)

    def hello(self, source):
        self.inputs[source] = 0

    def pulse(self, source, signal):
        self.received.add(source)
        self.inputs[source] = signal

        if self.type == ModuleType.BROADCASTER:
            for output in self.outputs:
                Module.events.append((self.name, signal, output))

        if self.type == ModuleType.CONJUCTION:
            conj = 1
            if all(self.inputs.values()):
                conj = 0

            for output in self.outputs:
                Module.events.append((self.name, conj, output))

        if self.type == ModuleType.FLIP_FLOP:
            if signal == 0:
                if self.state == 0:
                    self.state = 1
                else:
                    self.state = 0
                for output in self.outputs:
                    Module.events.append((self.name, self.state, output))

def parse(data):
    for line in data.strip().split('\n'):
        Module(line)

data = open('data', 'r').read()
parse(data)

Module.init()
while True:
    Module.pushButton()
