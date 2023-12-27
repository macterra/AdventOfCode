data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

def parse(lines):
    pairs = []
    for i in range(0, len(lines), 3):
        x = eval(lines[i])
        y = eval(lines[i+1])
        pairs.append((x,y))
    return pairs

def rightOrder(left, right):
    print(left, right)

    lInt = isinstance(left, int)
    rInt = isinstance(right, int)

    if lInt and rInt:
        if left == right:
            return 0
        elif left < right:
            return 1
        else:
            return -1

    if not (lInt or rInt):
        lLen = len(left)
        rLen = len(right)

        if lLen < rLen:
            for i in range(lLen):
                res = rightOrder(left[i], right[i])
                if res != 0:
                    return res
            return 1
        elif rLen < lLen:
            for i in range(rLen):
                res = rightOrder(left[i], right[i])
                if res != 0:
                    return res
            return -1
        else:
            for i in range(lLen):
                res = rightOrder(left[i], right[i])
                if res != 0:
                    return res
            return 0
    if lInt:
        return rightOrder([left], right)
    else:
        return rightOrder(left, [right])

data = open('data', 'r').read()
lines = data.split('\n')
pairs = parse(lines)

i = 1
sum = 0
for l, r in pairs:
    if rightOrder(l, r) == 1:
        sum += i
        print(i, 'right')
    else:
        print(i, 'wrong')
    i += 1

print(sum)
