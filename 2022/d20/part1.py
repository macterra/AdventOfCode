data = """1
2
-3
3
-2
0
4"""

data = open('data', 'r').read().strip()
lines = data.split('\n')
nums = [ int(line) for line in lines ]

class Wrapper:
    def __init__(self, val):
        self.val = val

    def __repr__(self) -> str:
        return str(self.val)

mixer = [ Wrapper(x) for x in nums ]
order = [ x for x in mixer ]

LEN = len(mixer)-1
for x in order:
    n = x.val
    i = mixer.index(x)
    j = i+n
    k = j%LEN
    mixer.remove(x)
    mixer.insert(k, x)

LEN = len(mixer)
for i in range(LEN):
    if mixer[i].val == 0:
        print(i)
        a = mixer[(i+1000) % LEN].val
        b = mixer[(i+2000) % LEN].val
        c = mixer[(i+3000) % LEN].val
        print(a, b, c, a+b+c)
        break

