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

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

open = pairs.keys()
close = pairs.values()

lines = input.split('\n')

print(lines)

def isCorrupt(line):
    stack = []
    for c in line:
        #print(c, c in open, c in close)
        if c in open:
            stack.append(c)
        else:
            x = stack.pop()
            #print('pop', x, pairs[x], c, pairs[x] == c)
            if pairs[x] != c:
                return score[c]
        #print(stack)
    return 0

sum = 0
for line in lines:
    sum += isCorrupt(line)
print(sum)
