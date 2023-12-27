import re
from collections import deque
from math import ceil

data = """\
Blueprint 1: Each ore robot minutess 4 ore. Each clay robot minutess 2 ore. Each obsidian robot minutess 3 ore and 14 clay. Each geode robot minutess 2 ore and 7 obsidian.
Blueprint 2: Each ore robot minutess 2 ore. Each clay robot minutess 3 ore. Each obsidian robot minutess 3 ore and 8 clay. Each geode robot minutess 3 ore and 12 obsidian."""

class Blueprint:
    def __init__(self, line):
        nums = [int(x) for x in re.findall(r'(\d+)', line)]
        self.id = nums.pop(0)
        self.costs = nums

def solve(maxt, costs):
    maxgeo = 0
    maxgeostate = ()
    oreoreCost, claoreCost, obsoreCost, obsclaCost, geooreCost, geoobsCost = costs
    maxoreBots = max(oreoreCost, claoreCost, obsoreCost, geooreCost)
    maxclaBots = obsclaCost
    maxobsBots = geoobsCost
    
    state = (1, 0, 0, 0, 0, 0, 0, 0)
    pqueue = deque([(0, state)])
    visited = set()

    while len(pqueue) > 0:
        minutes, state = pqueue.popleft()

        if minutes > maxt:
            continue
        
        #print(minutes, state, len(pqueue), maxgeo)

        if state in visited:
            continue

        visited.add(state)

        oreBots, claBots, obsBots, geoBots, ore, cla, obs, geo = state

        if geo > maxgeo:
            maxgeo = geo
            maxgeostate = state
            print(minutes, maxgeo, maxgeostate)

        if obsBots > 0: # make a geode bot
            needore = geooreCost - ore
            needobs = geoobsCost - obs
            t = 1 + max(0, ceil(needore/oreBots), ceil(needobs/obsBots))
            pqueue.append((minutes+t, (
                oreBots, claBots, obsBots, geoBots+1, 
                ore + t*oreBots - geooreCost, 
                cla + t*claBots, 
                obs + t*obsBots - geoobsCost, 
                geo + t*geoBots)))

        if claBots > 0 and obsBots < maxobsBots: # make an obsidian bot
            needore = obsoreCost - ore
            needcla = obsclaCost - cla
            t = 1 + max(0, ceil(needore/oreBots), ceil(needcla/claBots))
            pqueue.append((minutes+t, (
                oreBots, claBots, obsBots+1, geoBots, 
                ore + t*oreBots - obsoreCost, 
                cla + t*claBots - obsclaCost, 
                obs + t*obsBots, 
                geo + t*geoBots)))

        if claBots < maxclaBots: # make a clay bot
            needore = claoreCost - ore
            t = 1 + max(0, ceil(needore/oreBots))
            pqueue.append((minutes+t, (
                oreBots, claBots+1, obsBots, geoBots, 
                ore + t*oreBots - claoreCost, 
                cla + t*claBots, 
                obs + t*obsBots, 
                geo + t*geoBots)))

        if oreBots < maxoreBots: # make an ore bot
            needore = oreoreCost - ore
            t = 1 + max(0, ceil(needore/oreBots))
            pqueue.append((minutes+t, (
                oreBots+1, claBots, obsBots, geoBots,
                ore + t*oreBots - oreoreCost, 
                cla + t*claBots, 
                obs + t*obsBots, 
                geo + t*geoBots)))

        if geoBots > 0: # just collect geodes until end
            t = maxt - minutes
            pqueue.append((minutes+t, (
                oreBots, claBots, obsBots, geoBots, 
                ore + t*oreBots, 
                cla + t*claBots, 
                obs + t*obsBots, 
                geo + t*geoBots)))

    print(maxgeostate, maxgeo, len(visited))
    return maxgeo

data = open('data', 'r').read()
lines = data.split('\n')
blueprints = [ Blueprint(line) for line in lines ]

qlevel = 0
for bp in blueprints:
    qlevel += bp.id * solve(24, bp.costs)
print(qlevel)