input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

input = open('data', 'r').read()

lines = input.split('\n')
template = lines[0]

rules = {}
for line in lines[2:]:
    pair, insert = line.split(" -> ")
    rules[pair] = insert

# print(template)
# print(rules)

def apply(rules, template):
    out = []
    out.append(template[0])
    for i in range(len(template)-1):
        pair = template[i:i+2]
        #print(pair)
        #out.append(pair[0])
        if pair in rules:
            out.append(rules[pair])
        out.append(pair[1])
    #print(out)
    return "".join(out)

for i in range(10):
    template = apply(rules, template)
    print(f"After step {i+1}: {template} {len(template)}")

counts = []
for x in set(template):
    counts.append(len([c for c in template if c==x]))
counts = sorted(counts)
print(counts, counts[-1]-counts[0])
