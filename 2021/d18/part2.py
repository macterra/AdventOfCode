import json
import copy

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

def addAll(input):
    nums = [makeNum(x) for x in input.split('\n')]

    print(nums)
    res = reduce(nums[0], nums[1])
    for num in nums[2:]:
        res = reduce(res, num)
    return res

input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

input = open('data', 'r').read()

nums = [makeNum(x) for x in input.split('\n')]
count = len(nums)
print(nums)
maxmag = 0
for i in range(count):
    for j in range(i+1, count):
        mag1 = magnitude(reduce(nums[i], nums[j]))
        mag2 = magnitude(reduce(nums[j], nums[i]))
        maxmag = max(maxmag, mag1, mag2)
        print(i, j, mag1, mag2, maxmag)
