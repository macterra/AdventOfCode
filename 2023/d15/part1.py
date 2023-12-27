# https://adventofcode.com/2023/day/15

data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
data = open('data', 'r').read()

def hash(token):
    h = 0
    for c in token:
        h += ord(c)
        h *= 17
        h %= 256
    return h

tokens = data.strip().split(',')
print(tokens)
foo = [hash(token) for token in tokens]
print(foo)
print(sum(foo))
