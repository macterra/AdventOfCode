# https://adventofcode.com/2025/day/9

from functools import lru_cache

lines = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

lines = open('data', 'r').read()

# import input into list of tuples
input = []
for line in lines.strip().split('\n'):
    parts = line.split(',')
    input.append((int(parts[0]), int(parts[1])))

print(input)

# Convert input to tuple for memoization
input_tuple = tuple(input)

@lru_cache(maxsize=None)
def insideShape(corners, x, y):
    # determine if point (x, y) is inside of the shape defined by corners
    n = len(corners)
    inside = False
    p1x, p1y = corners[0]
    for i in range(n + 1):
        p2x, p2y = corners[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

@lru_cache(maxsize=None)
def onBorder(corners, x, y):
    # determine if point (x, y) is on the border of the shape defined by corners
    n = len(corners)
    p1x, p1y = corners[0]
    for i in range(n + 1):
        p2x, p2y = corners[i % n]
        # check if point (x, y) is on the line segment from (p1x, p1y) to (p2x, p2y)
        if min(p1x, p2x) <= x <= max(p1x, p2x) and min(p1y, p2y) <= y <= max(p1y, p2y):
            # check collinearity
            if (p2y - p1y) * (x - p1x) == (p2x - p1x) * (y - p1y):
                return True
        p1x, p1y = p2x, p2y
    return False

def segments_intersect(p1, p2, p3, p4):
    """Check if line segment p1-p2 intersects with line segment p3-p4"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return False  # Parallel or collinear

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom

    # Check if intersection point is within both segments
    return 0 <= t <= 1 and 0 <= u <= 1

def checkRectangle(corners, x1, y1, x2, y2):
    # Ensure x1 <= x2 and y1 <= y2
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Check all 4 corners first (fast rejection)
    rect_corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
    for (rx, ry) in rect_corners:
        if not (insideShape(corners, rx, ry) or onBorder(corners, rx, ry)):
            return False

    # Define rectangle edges
    rect_edges = [
        ((min_x, min_y), (max_x, min_y)),  # bottom
        ((max_x, min_y), (max_x, max_y)),  # right
        ((max_x, max_y), (min_x, max_y)),  # top
        ((min_x, max_y), (min_x, min_y)),  # left
    ]

    # Check if any polygon edge crosses through the rectangle interior
    n = len(corners)
    for i in range(n):
        p1 = corners[i]
        p2 = corners[(i + 1) % n]

        # Check if this polygon edge intersects any rectangle edge
        for rect_edge in rect_edges:
            if segments_intersect(p1, p2, rect_edge[0], rect_edge[1]):
                # Check if it's crossing through (not just touching at corners)
                # If both endpoints of polygon edge are outside rect, it crosses through
                p1_inside = (min_x <= p1[0] <= max_x and min_y <= p1[1] <= max_y)
                p2_inside = (min_x <= p2[0] <= max_x and min_y <= p2[1] <= max_y)

                # If one is inside and one outside, or both outside, it's crossing
                if not (p1_inside and p2_inside):
                    # This is a border touch/cross - need to check if it goes through interior
                    # Sample midpoint of the polygon edge
                    mid_x = (p1[0] + p2[0]) / 2
                    mid_y = (p1[1] + p2[1]) / 2

                    # If midpoint is strictly inside rectangle, reject
                    if min_x < mid_x < max_x and min_y < mid_y < max_y:
                        return False

    return True

min_x = min(c[0] for c in input)
max_x = max(c[0] for c in input)
min_y = min(c[1] for c in input)
max_y = max(c[1] for c in input)

# Build list of all candidate rectangles sorted by area (descending)
print("Building candidate list...")
candidates = []
for i in range(len(input)):
    x1, y1 = input[i]
    for j in range(i + 1, len(input)):
        x2, y2 = input[j]
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height
        candidates.append((area, x1, y1, x2, y2))

# Sort by area descending
candidates.sort(reverse=True)
print(f"Checking {len(candidates)} candidates...")

# Check candidates from largest to smallest
max_area = 0
for idx, (area, x1, y1, x2, y2) in enumerate(candidates):
    # Early exit if remaining candidates are too small
    if area <= max_area:
        print(f"Stopping early at candidate {idx}/{len(candidates)}")
        break

    if checkRectangle(input_tuple, x1, y1, x2, y2):
        print(f"Found valid rectangle: {area} from ({x1},{y1}) to ({x2},{y2})")
        max_area = area
        break  # Found the largest!

print(max_area)
