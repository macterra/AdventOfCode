# https://adventofcode.com/2025/day/10
# Integer Linear Programming approach

# Test with examples first
use_test = False

if use_test:
    lines = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
else:
    lines = open('data', 'r').read()

input_data = []
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
    input_data.append((pattern, buttons, joltage))

try:
    from scipy.optimize import milp, LinearConstraint, Bounds
    import numpy as np

    def solve_ilp_scipy(target, buttons):
        """Solve using scipy's MILP solver"""
        n_buttons = len(buttons)
        n_positions = len(target)

        # Build coefficient matrix: A[i,j] = amount button j adds to position i
        A = np.zeros((n_positions, n_buttons))
        for j, button in enumerate(buttons):
            for pos in button:
                A[pos, j] = 1

        # Objective: minimize sum of all button presses
        c = np.ones(n_buttons)

        # Constraints: A @ x == target (equality)
        constraints = LinearConstraint(A, target, target)

        # Bounds: x >= 0 (non-negative presses)
        bounds = Bounds(0, np.inf)

        # Solve with integrality constraint (all variables must be integers)
        integrality = np.ones(n_buttons)  # 1 = integer variable

        result = milp(c=c, constraints=constraints, bounds=bounds,
                     integrality=integrality)

        if result.success:
            # Verify the solution
            solution = np.round(result.x).astype(int)
            computed = A @ solution
            if not np.allclose(computed, target):
                print(f"    WARNING: Solution doesn't match! Got {computed}, expected {target}")
                print(f"    Solution vector: {solution}")
                print(f"    Result.x: {result.x}")
                return None
            # Return sum of rounded solution to be safe
            return int(np.sum(solution))
        else:
            print(f"    Solver failed with status: {result.status}, message: {result.message}")
        return None

    has_scipy = True
except ImportError:
    has_scipy = False
    print("scipy not available, trying pulp...")

try:
    import pulp

    def solve_ilp_pulp(target, buttons):
        """Solve using PuLP (pure Python ILP solver)"""
        n_buttons = len(buttons)
        n_positions = len(target)

        # Create problem
        prob = pulp.LpProblem("ButtonPress", pulp.LpMinimize)

        # Decision variables: how many times to press each button
        x = [pulp.LpVariable(f"button_{i}", lowBound=0, cat='Integer')
             for i in range(n_buttons)]

        # Objective: minimize total button presses
        prob += pulp.lpSum(x)

        # Constraints: sum of effects must equal target for each position
        for pos in range(n_positions):
            effect = pulp.lpSum(x[j] for j in range(n_buttons) if pos in buttons[j])
            prob += effect == target[pos], f"position_{pos}"

        # Solve
        prob.solve(pulp.PULP_CBC_CMD(msg=0))

        if prob.status == pulp.LpStatusOptimal:
            return int(pulp.value(prob.objective))
        return None

    has_pulp = True
except ImportError:
    has_pulp = False
    print("pulp not available either")

# Choose which solver to use
if has_scipy:
    print("Using scipy MILP solver")
    solve_func = solve_ilp_scipy
elif has_pulp:
    print("Using PuLP solver")
    solve_func = solve_ilp_pulp
else:
    print("ERROR: Need scipy or pulp for ILP solving")
    print("Install with: pip install scipy  OR  pip install pulp")
    exit(1)

# Solve all cases
total = 0
for i, (pattern, buttons, target) in enumerate(input_data, 1):
    if i <= 3:  # Show details for first 3
        print(f"\nCase {i}: target={target}, buttons={buttons}")
    else:
        print(f"\nCase {i}: target={target}, buttons={len(buttons)}")
    result = solve_func(target, buttons)
    if result is not None:
        print(f"  Solution: {result} presses")
        total += result
    else:
        print(f"  No solution found!")
        total += 0  # explicitly add 0 for clarity

print(f"\nTotal: {total}")
