# https://adventofcode.com/2024/day/5

input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def parseInput(input):
    rules, updates = input.split('\n\n')
    return parseRules(rules), parseUpdates(updates)

def parseRules(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    rules = {}
    for line in lines:
        a, b = line.split('|')
        a = int(a)
        b = int(b)
        if a in rules:
            rules[a].append(b)
        else:
            rules[a] = [b]
    return rules

def parseUpdates(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    updates = []
    for line in lines:
        updates.append([int(a) for a in line.split(',')])
    return updates

def checkOrder(rules, update):
    print(update)
    for i in range(1, len(update)):
        for j in range(i):
            a = update[i]
            b = update[j]
            print(i, j, a, b)
            if a in rules:
                if b in rules[a]:
                    print(f"oops {b} should come before {a} according to rules {rules[a]}")
                    return False
    return True


input = open('data', 'r').read()

rules, updates = parseInput(input)
print(rules, updates)

total = 0
for update in updates:
    if checkOrder(rules, update):
        total += update[len(update)//2]
print(total)