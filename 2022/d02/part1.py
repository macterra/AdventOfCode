data = """A Y
B X
C Z"""

scores = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

data = open('data', 'r').read()
lines = data.split('\n')

total = 0
for line in lines:
    print(line, scores[line])
    total += scores[line]

print(total)
