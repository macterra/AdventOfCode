data = """A Y
B X
C Z"""

scores = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,

    "B X": 1,
    "B Y": 5,
    "B Z": 9,

    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

data = open('data', 'r').read()
lines = data.split('\n')

total = 0
for line in lines:
    print(line, scores[line])
    total += scores[line]

print(total)
