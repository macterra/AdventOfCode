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

# Connect the 2 nodes that are closest to each other that are not already connected
def connect_closest_nodes(G):
    numNodes = G.number_of_nodes()
    min_dist = float('inf')
    min_edge = None
    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            if not G.has_edge(i, j):
                pos_i = G.nodes[i]['pos']
                pos_j = G.nodes[j]['pos']
                dist = ((pos_i[0] - pos_j[0]) ** 2 + (pos_i[1] - pos_j[1]) ** 2 + (pos_i[2] - pos_j[2]) ** 2) ** 0.5
                if dist < min_dist:
                    min_dist = dist
                    min_edge = (i, j)
    G.add_edge(min_edge[0], min_edge[1], weight=min_dist)
    print(f"Added edge {min_edge} with distance {min_dist}")

for i in range(1000):
    print(i)
    connect_closest_nodes(G)

# sort connected graphs by size
connected_components = list(nx.connected_components(G))
connected_components.sort(key=lambda x: len(x), reverse=True)

# multiply sizes of largest 3 connected components
result = 1
for component in connected_components[:3]:
    result *= len(component)
print("Result (product of sizes of largest 3 components):", result)
