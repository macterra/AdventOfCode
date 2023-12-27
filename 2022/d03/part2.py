data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

data = open('data', 'r').read()
lines = data.split('\n')

sum = 0
while lines:
    l1 = lines.pop()
    l2 = lines.pop()
    l3 = lines.pop()
    item = set(l1).intersection(set(l2)).intersection(set(l3)).pop()
    
    prio = ord(item) - ord('a') + 1
    if prio < 0:
        prio = ord(item) - ord('A') + 27
    sum += prio

    print(l1, l2, l3, item)

print(sum)
