import re
import time

import numpy as np
from pysat.card import ITotalizer
from pysat.solvers import Glucose3


SAMPLE = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
""".strip()


def parse_input(raw: str):
    blocks = raw.strip().split('\n\n')

    shapes: dict[int, list[list[str]]] = {}
    for block in blocks:
        lines = block.strip().split('\n')
        header = lines[0]
        match = re.match(r'(\d+):', header)
        if match:
            shape_id = int(match.group(1))
            grid = [list(line) for line in lines[1:]]
            shapes[shape_id] = grid

    region_lines = blocks[-1].strip().split('\n')
    regions: list[tuple[tuple[int, int], list[int]]] = []
    for line in region_lines:
        if not line.strip() or ':' not in line:
            continue
        parts = line.split(':')
        size = parts[0].strip()
        width, height = map(int, size.split('x'))
        presents = [int(x) for x in parts[1].strip().split(' ') if x]
        regions.append(((width, height), presents))

    return shapes, regions


try:
    RAW = open('data', 'r').read()
except FileNotFoundError:
    RAW = SAMPLE

shapes, regions = parse_input(RAW)


def create_tile(shape):
    # create a 2D numpy array from a shape grid
    return np.array([[1 if cell == '#' else 0 for cell in row] for row in shape])


def unique_orientations(tile: np.ndarray) -> list[np.ndarray]:
    orients: list[np.ndarray] = []
    for r in range(4):
        rot = np.rot90(tile, r)
        for flip in (False, True):
            t = np.fliplr(rot) if flip else rot
            if not any(t.shape == o.shape and np.array_equal(t, o) for o in orients):
                orients.append(t.copy())
    return orients


def _precompute_orient_coords(shapes_arr: dict[int, np.ndarray]):
    """Return per shape a list of orientations as (th, tw, filled_coords)."""
    out: dict[int, list[tuple[int, int, list[tuple[int, int]]]]] = {}
    for shape_id in range(6):
        tile = shapes_arr[shape_id]
        coords: list[tuple[int, int, list[tuple[int, int]]]] = []
        for orient in unique_orientations(tile):
            th, tw = orient.shape
            filled = [(dr, dc) for dr in range(th) for dc in range(tw) if orient[dr, dc] > 0]
            coords.append((th, tw, filled))
        out[shape_id] = coords
    return out


def _add_atmost1_seq(solver: Glucose3, lits: list[int], top_id: int) -> int:
    """Add an at-most-one constraint using a sequential counter (Sinz).

    This is much faster than calling CardEnc for every cell.
    """
    n = len(lits)
    if n <= 1:
        return top_id
    if n == 2:
        solver.add_clause([-lits[0], -lits[1]])
        return top_id

    # Aux vars s1..s_{n-1}
    s = list(range(top_id + 1, top_id + (n - 1) + 1))
    top_id += (n - 1)

    solver.add_clause([-lits[0], s[0]])
    for i in range(1, n - 1):
        solver.add_clause([-lits[i], s[i]])
        solver.add_clause([-s[i - 1], s[i]])
        solver.add_clause([-lits[i], -s[i - 1]])
    solver.add_clause([-lits[-1], -s[-1]])
    return top_id


def build_solver_for_size(
    region_size: tuple[int, int],
    shapes_arr: dict[int, np.ndarray],
    max_counts: list[int],
):
    """Build a SAT solver for a fixed (W,H).

    Variables represent selecting a placement of a shape (shape id, orientation, top-left position).
    Constraints:
      - For each grid cell: at most one selected placement covers it.
      - For each shape id: exactly `count` placements are selected.

    The overlap constraints and the cardinality encodings are built once per size.
    Each query (a concrete `presents` list) is answered using assumptions over totalizer outputs.
    """

    W, H = region_size
    area = W * H

    if W < 1 or H < 1:
        return None

    # All shapes are defined in 3x3; if region too small to fit any present, only the all-zero request is feasible.
    if W < 3 or H < 3:
        if any(max_counts):
            return None
        return {
            'solver': Glucose3(),
            'rhs_by_shape': [[] for _ in range(6)],
            'W': W,
            'H': H,
            'shape_lits_lens': [0] * 6,
        }

    orient_coords = _precompute_orient_coords(shapes_arr)

    # Build placement literals.
    next_var = 1
    shape_lits: list[list[int]] = [[] for _ in range(6)]
    cell_to_lits: list[list[int]] = [[] for _ in range(area)]

    for shape_id in range(6):
        for th, tw, filled in orient_coords[shape_id]:
            if th > H or tw > W:
                continue
            for r0 in range(H - th + 1):
                row_base = r0 * W
                for c0 in range(W - tw + 1):
                    lit = next_var
                    next_var += 1
                    shape_lits[shape_id].append(lit)
                    base = row_base + c0
                    for dr, dc in filled:
                        cell_to_lits[base + dr * W + dc].append(lit)

    top_id = next_var - 1

    # Quick sanity: if a shape has zero placements, it can only be satisfied with count 0.
    for sid in range(6):
        if not shape_lits[sid] and max_counts[sid] > 0:
            return None

    solver = Glucose3()

    # Overlap constraints: for each cell, at most one placement covering it.
    for lits in cell_to_lits:
        if len(lits) <= 1:
            continue
        top_id = _add_atmost1_seq(solver, lits, top_id)

    # Per-shape exact-count constraints: build totalizer once, query using assumptions.
    rhs_by_shape: list[list[int]] = [[] for _ in range(6)]
    for sid in range(6):
        ub = max_counts[sid]
        if ub <= 0:
            continue
        # Also impossible if request exceeds number of placements.
        if ub > len(shape_lits[sid]):
            return None

        t = ITotalizer(lits=shape_lits[sid], ubound=ub, top_id=top_id)
        top_id = t.top_id
        solver.append_formula(t.cnf.clauses)
        rhs_by_shape[sid] = t.rhs

    return {
        'solver': solver,
        'rhs_by_shape': rhs_by_shape,
        'W': W,
        'H': H,
        'shape_lits_lens': [len(x) for x in shape_lits],
    }


def pack_presents(prebuilt, region_size: tuple[int, int], presents: list[int]) -> bool:
    W, H = region_size
    area = W * H
    total_tiles = sum(presents)

    # Fast necessary checks.
    if total_tiles == 0:
        return True
    if 7 * total_tiles > area:
        return False

    rhs_by_shape: list[list[int]] = prebuilt['rhs_by_shape']
    assumptions: list[int] = []

    for sid, count in enumerate(presents[:6]):
        # If there is no totalizer built (max_count was 0), only count 0 is allowed.
        rhs = rhs_by_shape[sid]
        if not rhs:
            if count != 0:
                return False
            continue

        # Totalizer rhs semantics:
        #   rhs[k] means sum(lits) >= k+1
        # Enforce exactly `count` by:
        #   sum >= count  => rhs[count-1] (if count>0)
        #   sum <= count  => -rhs[count]   (if count < ubound)
        ub = len(rhs) - 1
        if count > ub:
            return False
        if count == 0:
            assumptions.append(-rhs[0])
        else:
            assumptions.append(rhs[count - 1])
            if count < ub:
                assumptions.append(-rhs[count])

    return bool(prebuilt['solver'].solve(assumptions=assumptions))


shapes_arr = {sid: create_tile(grid) for sid, grid in shapes.items()}

# Group regions by size so we can build/reuse one solver per size.
regions_by_size: dict[tuple[int, int], list[list[int]]] = {}
max_counts_by_size: dict[tuple[int, int], list[int]] = {}
for size, presents in regions:
    regions_by_size.setdefault(size, []).append(presents)

for size, pres_list in regions_by_size.items():
    max_counts = [0] * 6
    for pres in pres_list:
        for i in range(min(6, len(pres))):
            if pres[i] > max_counts[i]:
                max_counts[i] = pres[i]
    max_counts_by_size[size] = max_counts


print("Regions to assemble:")
count_true = 0
count_false = 0
idx = 0

# Process sizes in a stable order for reproducible timing.
for size in sorted(regions_by_size.keys()):
    pres_list = regions_by_size[size]
    prebuilt = build_solver_for_size(size, shapes_arr, max_counts_by_size[size])
    if prebuilt is None:
        for pres in pres_list:
            idx += 1
            count_false += 1
            print(f"  {idx}. ✗ Size: {size}, Presents: {pres}, Time: 0.000s")
        continue

    for pres in pres_list:
        idx += 1
        start = time.time()
        fits = pack_presents(prebuilt, size, pres)
        elapsed = time.time() - start
        if fits:
            count_true += 1
        else:
            count_false += 1
        status = "✓" if fits else "✗"
        print(f"  {idx}. {status} Size: {size}, Presents: {pres}, Time: {elapsed:.3f}s")

print(f"\nSummary: {count_true} True, {count_false} False")
