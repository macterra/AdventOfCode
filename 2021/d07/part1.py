input = "16,1,2,0,4,2,7,1,2,14"
input = open('data', 'r').read()
crabs = [int(x) for x in input.split(',')]

print(crabs)

def fuel(pos):
    sum = 0
    for crab in crabs:
        sum += abs(crab - pos)
    return sum

a = min(crabs)
b = max(crabs)

cost = [fuel(x) for x in range(a,b+1)]

print(min(cost))