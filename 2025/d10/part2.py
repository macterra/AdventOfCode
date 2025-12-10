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
    joltages = parts[-1].strip('{}')
    joltage = [int(x) for x in joltages.split(',')]
    input.append((pattern, buttons, joltage))

#print(input)

from functools import lru_cache

def solve_bruteforce_smart(endState, buttons):
    """Try all combinations of button presses with memoization"""
    n_buttons = len(buttons)
    n_positions = len(endState)
    endState_tuple = tuple(endState)
    buttons_tuple = tuple(buttons)

    # Upper bound: sum of all target values (very pessimistic)
    max_total = sum(endState)

    print(f"Searching up to {max_total} total presses for target {endState}")

    # Memoized recursive function
    @lru_cache(maxsize=None)
    def try_combinations(remaining_presses, button_idx, current_state):
        if button_idx == n_buttons:
            if remaining_presses == 0 and current_state == endState_tuple:
                return 0  # Found solution, no more presses needed
            return None

        # Pruning: if current state already exceeds target anywhere, skip
        if any(current_state[i] > endState_tuple[i] for i in range(n_positions)):
            return None

        # Try 0 to remaining_presses for this button
        for count in range(remaining_presses + 1):
            # Calculate new state after pressing this button 'count' times
            new_state = list(current_state)
            for _ in range(count):
                for pos in buttons_tuple[button_idx]:
                    if pos < n_positions:
                        new_state[pos] += 1

            new_state_tuple = tuple(new_state)

            # Early pruning: if we've exceeded target, skip
            if any(new_state_tuple[i] > endState_tuple[i] for i in range(n_positions)):
                # No point trying more presses of this button
                break

            result = try_combinations(
                remaining_presses - count,
                button_idx + 1,
                new_state_tuple
            )
            if result is not None:
                return count + result
        return None

    # Try increasing total press counts
    for total_presses in range(1, max_total + 1):
        if total_presses % 5 == 0:
            print(f"  Trying total_presses = {total_presses}")

        initial_state = tuple([0] * n_positions)
        result = try_combinations(total_presses, 0, initial_state)
        if result is not None:
            return result

    return float('inf')


total = 0
for pattern, buttons, joltage in input:
    # Convert buttons list to tuple for hashability
    buttons_tuple = tuple(buttons)
    result = solve_bruteforce_smart(joltage, buttons_tuple)
    print(f"Joltage: {joltage}, Minimum Presses: {result}")
    total += result

print("Total Sum of Minimum Presses:", total)
