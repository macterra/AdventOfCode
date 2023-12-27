import numpy as np

input = "3,4,3,1,2"
input = open('data', 'r').read()

fish = [int(x) for x in input.split(',')]

print(fish)

ages = [0] * 9
for f in fish:
    ages[f] += 1

print(0, ages)
for d in range(256):
    x = ages[0]
    for i in range(8):
        ages[i] = ages[i+1]
    ages[6] += x
    ages[8] = x
    print(d+1, ages)
print(sum(ages))