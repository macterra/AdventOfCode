import numpy as np

input = "3,4,3,1,2"
#input = open('data', 'r').read()

fish = [int(x) for x in input.split(',')]

print(fish)

for d in range(80):
    fish = [f-1 for f in fish]
    spawn = []
    for i in range(len(fish)):
        if fish[i] == -1:
            spawn.append(8)
            fish[i] = 6
    fish.extend(spawn)            
    print(d+1, len(fish))
