p1 = 4
p2 = 8
#p2 = 10

rolls = { 3:1, 4:3, 5:27, 6:81, 7:27, 8:9, 9:1 }

class Player:
    def __init__(self, pos, score, count, steps):
        self.pos = pos
        self.score = score
        self.count = count
        self.steps = steps

    def __repr__(self):
        return f"Player(pos={self.pos} score={self.score} count={self.count} steps={self.steps})"

def simulate(pos1):
    players = [ Player(pos1-1, 0, 1, 0) ]        

    finish = []
    while len(players) > 0:
        next = []
        for p in players:
            #print(p)
            for roll, c in rolls.items():
                #print(roll, c)
                pos = (p.pos + roll) % 10
                score = p.score + pos + 1
                count = p.count * c
                steps = p.steps + 1
                clone = Player(pos, score, count, steps)
                if score >= 21:
                    finish.append(clone)
                else:
                    next.append(clone)                
        players = next

    total = {}
    for p in finish:
        if not p.steps in total:
            total[p.steps] = p.count
        else:
            total[p.steps] += p.count
    print(total)  
    return total

t1 = simulate(4)
t2 = simulate(8)

x = 0
y = 0
for s1 in t1:
    for s2 in t2:
        if s1 <= s2:
            x += t1[s1]
        else:
            y += t1[s2]
print(x, y)
