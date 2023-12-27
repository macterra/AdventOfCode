# https://adventofcode.com/2023/day/20

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

class Module:
    modules = {}
    events = []
    outputs = []
    lows = 0
    highs = 0

    @classmethod
    def connectAll(cls):
        for name in cls.modules:
            cls.modules[name].connect()
        for name in cls.outputs:
            Module(f"{name} -> ")

    @classmethod
    def resetAll(cls):
        for name in cls.modules:
            cls.modules[name].reset()

    @classmethod
    def pushButton(cls):
        cls.events.append(('button', 0, 'broadcaster'))

    @classmethod
    def tick(cls):
        while cls.events:
            source, signal, target = cls.events[0]
            del cls.events[0]
            cls.modules[target].pulse(source, signal)
            if signal:
                cls.highs += 1
            else:
                cls.lows +=1

    def __init__(self, spec):
        name, outputs = spec.split(' -> ')

        self.name = name
        self.kind = 0
        self.state = 0
        self.received = set()

        if name[0] == '&':
            self.kind = 1
            self.name = name[1:]

        if name[0] == '%':
            self.kind = 2
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

    def reset(self):
        self.received = set()

    def pulse(self, source, signal):
        foo = 'high' if signal else 'low'
        print(f"{source} -{foo}-> {self.name}")
        self.received.add(source)
        self.inputs[source] = signal

        if self.kind == 0: # Broadcaster
            for output in self.outputs:
                Module.events.append((self.name, signal, output))

        if self.kind == 1: # & Conjuction
            conj = 1
            if all(self.inputs.values()):
                conj = 0

            for output in self.outputs:
                Module.events.append((self.name, conj, output))

        if self.kind == 2: # % Flip-flop
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
    Module.connectAll()

data = open('data', 'r').read()
parse(data)

for name in Module.modules:
    print(name, Module.modules[name])

for i in range(1000):
    Module.pushButton()
    Module.tick()
print(Module.lows, Module.highs, Module.lows * Module.highs)

