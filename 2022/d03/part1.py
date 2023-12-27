data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

data = open('data', 'r').read()
lines = data.split('\n')

sum = 0
for line in lines:
    l = len(line)
    l = int(l/2)
    com1 = set(line[:l])
    com2 = set(line[l:])
    item = com1.intersection(com2).pop()
    prio = ord(item) - ord('a') + 1
    if prio < 0:
        prio = ord(item) - ord('A') + 27
    sum += prio
    print(line, l, com1, com2, item, prio)
    
print(sum)