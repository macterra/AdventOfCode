input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

input = open('data', 'r').read()

pairs = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}'
}

invpairs = {v: k for k, v in pairs.items()}

score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

open = pairs.keys()
close = pairs.values()

lines = input.split('\n')

print(lines)

def isCorrupt(line):
    stack = []
    for c in line:
        if c in open:
            stack.append(c)
        else:
            x = stack.pop()
            if pairs[x] != c:
                return True
    return False

def complete(line):
    print(line)
    line = line[::-1]
    stack = []
    comp = []
    for c in line:
        if c in close:
            stack.append(c)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                comp.append(pairs[c])
    sum = 0
    for c in comp:
        sum = sum*5 + score[c]
    print('comp', "".join(comp), sum)
    return sum

scores = []
for line in lines:
    if not isCorrupt(line):
        scores.append(complete(line))
print(scores)
scores = sorted(scores)
l = len(scores)
print(scores[int(l/2)])
