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

def makePairs(template):
    pairs = {}
    for i in range(len(template)-1):
        pair = template[i:i+2]
        pairs[pair] = 1
    return pairs

def apply2(rules, pairs):
    next = {}
    for pair in pairs.keys():
        if pair in rules:
            count = pairs[pair]
            if count > 0:
                insert = rules[pair]

                pair1 = f"{pair[0]}{insert}"

                if not pair1 in next:
                    next[pair1] = count
                else:
                    next[pair1] += count

                pair2 = f"{insert}{pair[1]}"

                if not pair2 in next:
                    next[pair2] = count
                else:
                    next[pair2] += count
        else:
            next[pair] = 1
    return next

def method1(rules, template, steps):
    print(f"After step 0: {template} {len(template)}")
    for i in range(steps):
        template = apply(rules, template)
        print(f"After step {i+1}: {template} {len(template)}")

    counts = []
    for x in set(template):
        counts.append(len([c for c in template if c==x]))
    counts = sorted(counts)
    print(counts, counts[-1]-counts[0])

def method2(rules, template, steps):
    pairs = makePairs(template)
    print(pairs)

    print(f"After step 0: {pairs}")
    for i in range(steps):
        pairs = apply2(rules, pairs)
        print(f"After step {i+1}: {pairs}")

    counts = {}
    for pair in pairs:
        c = pair[0]
        if c in counts:
            counts[c] += pairs[pair]
        else:
            counts[c] = pairs[pair]
    counts[template[-1]] += 1
    counts = counts.values()
    counts = sorted(counts)
    print(counts)
    print(counts, counts[-1]-counts[0])   

#method1(rules, template, 10)
method2(rules, template, 40)
