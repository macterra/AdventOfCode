# https://adventofcode.com/2025/day/8

import networkx as nx

lines = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

lines = open('data', 'r').read()

# import input into list of tuples
input = []
for line in lines.strip().split('\n'):
    parts = line.split(',')
    input.append((int(parts[0]), int(parts[1]), int(parts[2])))


print(input)

# build a graph including all nodes in the input
G = nx.Graph()
for i in range(len(input)):
    G.add_node(i, pos=input[i])

print(G)

# Precompute all distances and create a complete graph
numNodes = G.number_of_nodes()
for i in range(numNodes):
    pos_i = input[i]
    for j in range(i + 1, numNodes):
        pos_j = input[j]
        dist = ((pos_i[0] - pos_j[0]) ** 2 + (pos_i[1] - pos_j[1]) ** 2 + (pos_i[2] - pos_j[2]) ** 2) ** 0.5
        G.add_edge(i, j, weight=dist)

# Use Kruskal's algorithm to find MST
mst = nx.minimum_spanning_tree(G)

# Find the last edge added (the one with maximum weight in the MST)
max_weight = 0
max_edge = None
for u, v, data in mst.edges(data=True):
    if data['weight'] > max_weight:
        max_weight = data['weight']
        max_edge = (u, v)

pos1 = input[max_edge[0]]
pos2 = input[max_edge[1]]
print(f"Final edge connects nodes at positions {pos1} and {pos2}")
print(f"Maximum edge weight: {max_weight}")
print(pos1[0] * pos2[0])

