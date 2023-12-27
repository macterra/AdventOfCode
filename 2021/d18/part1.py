import json
import copy

input = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"""

input = """[[[[[9,8],1],2],3],4]
[7,[6,[5,[4,[3,2]]]]]
[[6,[5,[4,[3,2]]]],1]
[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"""

class Item:
    def __init__(self, val, dep):
        self.val = val
        self.dep = dep
    
    def __repr__(self):
        return f"<{self.val} {self.dep}>"

def flatten(num, dep, flat):
    if isinstance(num, int):
        flat.append(Item(num, dep))
    else:
        for i in num:
            flatten(i, dep+1, flat)
    return flat

def add(n1, n2):
    sum = copy.deepcopy(n1 + n2)
    for i in sum:
        i.dep += 1
    return sum

def explode(num):
    count = len(num)
    for i in range(count):
        if num[i].dep > 4:
            if i > 0:
                num[i-1].val += num[i].val
            if i < count-2:
                num[i+2].val += num[i+1].val
            num.insert(i, Item(0,num[i].dep-1))
            del num[i+1:i+3]
            return True
    return False

def split(num):
    count = len(num)
    for i in range(count):
        val = num[i].val
        dep = num[i].dep
        if val >= 10:
            del num[i]
            num.insert(i, Item(int(val/2 + 0.5), dep+1))
            num.insert(i, Item(int(val/2), dep+1))
            return True
    return False

def reduce(num1, num2):
    num3 = add(num1, num2)
    
    while explode(num3) or split(num3):
        pass

    return num3

def makeNum(input):
    return flatten(json.loads(input), 0, [])

def test1():
    lines = input.split('\n')
    for line in lines:
        x = json.loads(line)
        f = flatten(x, 0, [])
        print(x)
        print(f)
        ex = explode(f)
        print(ex, f)
        print()

def test2():
    num1 = makeNum("[[[[4,3],4],4],[7,[[8,4],9]]]")
    num2 = makeNum("[1,1]")
    num3 = add(num1, num2)

    print(num1)
    print(num2)
    print(num3)

    ex = explode(num3)
    print(num3)

    ex = explode(num3)
    print(num3)

    sp = split(num3)
    print(num3)

    sp = split(num3)
    print(num3)

    ex = explode(num3)
    print("test2", num3)

def test3():
    num1 = makeNum("[[[[4,3],4],4],[7,[[8,4],9]]]")
    num2 = makeNum("[1,1]")
    num3 = add(num1, num2)

    print(num1)
    print(num2)
    print(num3)

    while explode(num3) or split(num3):
        pass

    print("test3", num3)

def test4():
    num1 = makeNum("[[[[4,3],4],4],[7,[[8,4],9]]]")
    num2 = makeNum("[1,1]")
    print("test4", reduce(num1, num2))

def test5(input, check):
    nums = [makeNum(x) for x in input.split('\n')]
    check = makeNum(check)

    print(nums)
    res = reduce(nums[0], nums[1])
    for num in nums[2:]:
        res = reduce(res, num)
    print(res)
    print(check)

input1 = """[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]"""

check1 = "[[[[5,0],[7,4]],[5,5]],[6,6]]"

input2 = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""

check2 = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"

input3 = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

check3 = "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"

#test5(input2, check2)

def magnitude(num):
    nums = copy.deepcopy(num)
    count = len(nums)

    while count > 1:
        for i in range(1, count):
            prev = nums[i-1]
            this = nums[i]
            if prev.dep == this.dep:
                mag = prev.val * 3 + this.val * 2
                rep = Item(mag, this.dep-1)
                del nums[i-1:i+1]
                nums.insert(i-1, rep)
                count = len(nums)
                break
    return nums[0].val

"""
[[1,2],[[3,4],5]] becomes 143.
[[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
[[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
[[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
[[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.
"""
def test6():
    n = makeNum("[[1,2],[[3,4],5]]")
    print(n, magnitude(n), 143)

    n = makeNum("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
    print(n, magnitude(n), 1384)

    n = makeNum("[[[[1,1],[2,2]],[3,3]],[4,4]]")
    print(n, magnitude(n), 445)

    n = makeNum("[[[[3,0],[5,3]],[4,4]],[5,5]]")
    print(n, magnitude(n), 791)

    n = makeNum("[[[[5,0],[7,4]],[5,5]],[6,6]]")
    print(n, magnitude(n), 1137)

    n = makeNum("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
    print(n, magnitude(n), 3488)



def addAll(input):
    nums = [makeNum(x) for x in input.split('\n')]

    print(nums)
    res = reduce(nums[0], nums[1])
    for num in nums[2:]:
        res = reduce(res, num)
    return res

input = open('data', 'r').read()
homework = addAll(input)
print(homework, magnitude(homework))
