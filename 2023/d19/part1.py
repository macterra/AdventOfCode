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

class Part:
    def __init__(self, spec):
        vals = spec[1:-1].split(',')
        self.vals = {
            'x': int(vals[0][2:]),
            'm': int(vals[1][2:]),
            'a': int(vals[2][2:]),
            's': int(vals[3][2:])
        }

    def total(self):
        return sum(self.vals.values())

    def __repr__(self):
        return f"Part {self.vals}>"

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
    rules, parts = data.strip().split('\n\n')
    rules = rules.split('\n')
    rules = [Rule(spec) for spec in rules]
    rules = {rule.name: rule for rule in rules}
    parts = parts.split('\n')
    parts = [Part(spec) for spec in parts]
    return rules, parts

def apply(rules, part):
    nextRule = 'in'
    while True:
        nextRule = rules[nextRule].apply(part)
        if nextRule in ['A', 'R']:
            return nextRule == 'A'

data = open('data', 'r').read()
rules, parts = parse(data)

total = 0
for part in parts:
    if apply(rules, part):
        total += part.total()
print(total)
