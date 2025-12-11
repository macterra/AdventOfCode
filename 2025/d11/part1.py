# https://adventofcode.com/2025/day/11

lines = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
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

# count all the paths from you to out
def count_paths(device, memo={}):
    if device in memo:
        return memo[device]
    if device == 'out':
        return 1
    total_paths = 0
    for output in devices.get(device, []):
        total_paths += count_paths(output, memo)
    memo[device] = total_paths
    return total_paths

total = count_paths('you')
print("Total paths from 'you' to 'out':", total)
