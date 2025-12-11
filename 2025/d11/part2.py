# https://adventofcode.com/2025/day/11

lines = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

lines = open('data', 'r').read()

input = lines.strip().split('\n')

devices = {}
for line in input:
    parts = line.split(':')
    name = parts[0].strip()
    outputs = parts[1].strip().split(' ')
    devices[name] = [out.strip() for out in outputs if out.strip()]

print("Devices and their outputs:")
for name, outputs in devices.items():
    print(f"  {name} -> {outputs}")

from functools import lru_cache

# Build reverse graph for backward search
reverse_graph = {}
for node, outputs in devices.items():
    for output in outputs:
        if output not in reverse_graph:
            reverse_graph[output] = []
        reverse_graph[output].append(node)

@lru_cache(maxsize=None)
def count_paths_states(current, state):
    """
    Count paths from current to 'out' in a given state.
    state: 0 = neither seen, 1 = fft seen, 2 = dac seen, 3 = both seen
    """
    # Update state based on current node
    if current == 'fft' and state in (0, 2):
        state = 1 if state == 0 else 3
    if current == 'dac' and state in (0, 1):
        state = 2 if state == 0 else 3

    # Reached destination
    if current == 'out':
        return 1 if state == 3 else 0

    # Dead end
    if current not in devices:
        return 0

    # Sum paths through all neighbors (no visited tracking - DAG assumed or handle differently)
    total = 0
    for node in devices[current]:
        total += count_paths_states(node, state)

    return total

total = count_paths_states('svr', 0)
print("Total paths including both 'fft' and 'dac':", total)
