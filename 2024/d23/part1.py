# https://adventofcode.com/2024/day/23

import networkx as nx
from itertools import combinations

input = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

input = open('data', 'r').read()

def parse(input):
    lines = [line for line in input.split('\n') if line.strip() != '']
    graph = nx.Graph()
    for line in lines:
        a, b = line.split('-')
        graph.add_edge(a, b)
    return graph

graph = parse(input)
print(graph)

triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]

total = 0
for triangle in triangles:
    for node in triangle:
        if node[0] == 't':
            total += 1
            break
print(total)
