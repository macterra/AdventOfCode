# https://adventofcode.com/2024/day/22

input = """
1
10
100
2024
"""

input = open('data', 'r').read()
initial = [int(i) for i in input.split('\n') if i.strip() != '']

print(initial)

def pseudo(x):
    x = (x ^ 64*x) % 16777216
    x = (x ^ (x // 32)) % 16777216
    x = (x ^ 2048*x)  % 16777216
    return x

secrets = initial
for i in range(2000):
    secrets = [pseudo(x) for x in secrets]
    #print(i, secrets)
print(sum(secrets))
