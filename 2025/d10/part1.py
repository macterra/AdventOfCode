# https://adventofcode.com/2025/day/10

lines = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

lines = open('data', 'r').read()

input = []
for line in lines.strip().split('\n'):
    parts = line.split(' ')
    pattern = parts[0].strip('[]')
    buttons = []
    for i in range(1, len(parts) - 1):
        pos_part = parts[i].strip('()')
        pos_tuple = tuple(int(x) for x in pos_part.split(','))
        buttons.append(pos_tuple)
    counts_part = parts[-1].strip('{}')
    counts = [int(x) for x in counts_part.split(',')]
    input.append((pattern, buttons, counts))

print(input)

from functools import lru_cache

@lru_cache(maxsize=None)
def search(endState, buttons, state, depth=0, max_depth=20):
    if state == endState:
        return 0

    if depth >= max_depth:
        return float('inf')

    min_presses = float('inf')
    for button in buttons:
        new_state = list(state)
        for pos in button:
            if pos < len(new_state):
                new_state[pos] = '#' if new_state[pos] == '.' else '.'
        new_state_str = ''.join(new_state)
        presses = 1 + search(endState, buttons, new_state_str, depth + 1, max_depth)
        if presses < min_presses:
            min_presses = presses

    return min_presses


sum = 0
for pattern, buttons, counts in input:
    initial_state = '.' * len(pattern)
    # Convert buttons list to tuple for hashability
    buttons_tuple = tuple(buttons)
    result = search(pattern, buttons_tuple, initial_state)
    print(f"Pattern: {pattern}, Minimum Presses: {result}")
    sum += result

print("Total Sum of Minimum Presses:", sum)
