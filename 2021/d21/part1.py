input1 = """Player 1 starting position: 4
Player 2 starting position: 8"""

input2 = """Player 1 starting position: 4
Player 2 starting position: 10"""

def playerPositions(input):
    lines = input.split('\n')
    _, p1 = lines[0].split(':')
    _, p2 = lines[1].split(':')
    return int(p1), int(p2)


class DiracDice:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.s1 = 0
        self.p2 = p2
        self.s2 = 0
        self.rolls = 0
        self.die = 1

    def __repr__(self):
        return f"DiracDice: player1 pos={self.p1} score={self.s1}, player2 pos{self.p2} score={self.s2}"

    def roll(self):
        d = self.die
        self.die = (self.die+1)%100
        d += self.die
        self.die = (self.die+1)%100        
        d += self.die
        self.die = (self.die+1)%100
        self.rolls += 3
        return d

    def play(self):
        r = self.roll()
        self.p1 = (self.p1-1 + r)%10 + 1
        self.s1 += self.p1
        print(self)

        if self.done():
            return

        r = self.roll()
        self.p2 = (self.p2-1 + r)%10 + 1
        self.s2 += self.p2
        print(self)

    def done(self):
        top = max(self.s1, self.s2)
        return top >= 1000

    def go(self):
        while not self.done():
            self.play()
        return self.rolls * min(self.s1, self.s2)

p1, p2 = playerPositions(input2)  
dd = DiracDice(p1, p2)
print(dd)
print(dd.go())
