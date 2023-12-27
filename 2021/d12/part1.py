input0 = """start-A
start-b
A-end
b-end"""

input1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

input2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

input3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

input4 = """xq-XZ
zo-yr
CT-zo
yr-xq
yr-LD
xq-ra
np-zo
end-LD
np-LD
xq-kq
start-ra
np-kq
LO-end
start-xq
zo-ra
LO-np
XZ-start
zo-kq
LO-yr
kq-XZ
zo-LD
kq-ra
XZ-yr
LD-ws
np-end
kq-yr"""

class Cave:
    def __init__(self, name):
        self.name = name
        self.big = name[0].isupper()
        self.links = []

    def __str__(self):
        return f"{self.name} {self.big} {self.links}"

    def __repr__(self):
        return f"{self.name}"

def makeGraph(input):
    graph = {}

    for line in input.split('\n'):
        a, b = line.split('-')

        if a in graph:
            ca = graph[a]
        else:
            ca = Cave(a)
            graph[a] = ca

        if b in graph:
            cb = graph[b]
        else:
            cb = Cave(b)
            graph[b] = cb

        ca.links.append(b)
        cb.links.append(a)

        print('ca', ca)
        print('cb', cb)
        
    return graph

def findPath(graph, name, path, paths):
    print(f"findPath {name} {path}")

    if 'end' in path:
        paths.append(path)
        return path

    cave = graph[name]

    if cave.big or not name in path:
        path.append(name)

        for link in cave.links:
            p = findPath(graph, link, path.copy(), paths)
            print(p)
            if 'end' in path:
                break

    return path

graph = makeGraph(input4)
print(graph)

paths = []
path = findPath(graph, 'start', [], paths)
print(paths)

for path in paths:
    print(",".join(path))

print(int(len(paths)))
