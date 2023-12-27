# https://adventofcode.com/2023/day/19

import re

data = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

class Rule:
    def __init__(self, spec):
        pattern = re.compile(r'(\w+)\{(.+?)\}')
        match = pattern.match(spec)
        if match:
            self.name = match.group(1)
            self.conditions = []
            for condition in match.group(2).split(','):
                if condition.find(':') < 0:
                    self.conditions.append((True, condition))
                else:
                    condition, name = condition.split(':')
                    self.conditions.append(((condition[0], condition[1], int(condition[2:])), name))

    def __repr__(self):
        return f"Rule<{self.name} conditions={self.conditions}>"

    def apply(self, part):
        for condition, nextRule in self.conditions:
            if isinstance(condition, tuple):
                prop, op, val = condition
                if op == '<':
                    if part.vals[prop] < val:
                        return nextRule
                else:
                    if part.vals[prop] > val:
                        return nextRule
            else:
                return nextRule

def parse(data):
    rules, _ = data.strip().split('\n\n')
    rules = rules.split('\n')
    rules = [Rule(spec) for spec in rules]
    rules = {rule.name: rule for rule in rules}
    return rules

def simulate(rules, name, part, path):
    print(f"simulate {name} {part} {path}")

    if name == 'A':
        xa, xb = part['x']
        ma, mb = part['m']
        aa, ab = part['a']
        sa, sb = part['s']
        ways = (xb - xa + 1) * (mb - ma + 1) * (ab - aa + 1) * (sb - sa + 1)
        print('ways', ways)
        return ways
    if name == 'R':
        return 0

    path = path + [name]
    rule = rules[name]
    total = 0

    for condition, next in rule.conditions:
        if isinstance(condition, tuple):
            prop, op, val = condition
            a, b = part[prop]
            if op == '<':
                if a < val:
                    part2 = dict(part)
                    part2[prop] = (a, min(b, val-1))
                    total += simulate(rules, next, part2, path)
                a = max(a, val)
                part[prop] = (a, b)
            else:
                if b > val:
                    part2 = dict(part)
                    part2[prop] = (max(a, val+1), b)
                    total += simulate(rules, next, part2, path)
                b = min(b, val)
                part[prop] = (a, b)
        else:
            total += simulate(rules, next, part, path)
    return total

data = open('data', 'r').read()
rules = parse(data)

vals = {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000),
}

print(simulate(rules, 'in', vals, []))

"""
mine:    167409079868000
correct  167409079868000
"""
