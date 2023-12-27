import networkx as nx

data = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

def parse(data):
    graph = nx.Graph()
    for line in data.strip().split("\n"):
        p = line.split()
        for t in p[1:]:
            graph.add_edge(p[0][:-1],t)
    return graph

data = open('data', 'r').read()
graph = parse(data)
cv, p = nx.stoer_wagner(graph)
print(len(p[0])*len(p[1]))
