import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
rows = [line.strip() for line in open(infile)]


def print_map(rows, seen):
    print("   ", end="")
    for number in range(0, len(rows[0])):
        print(number, end=" ")

    print()
    for ri, row in enumerate(rows):
        print(ri, end="  ")
        for ci, c in enumerate(row):
            if (ri, ci) in [loc for loc, ray in seen]:
                print("#", end=" ")
            else:
                print(c, end=" ")
        print()


def get_all_rays(start):
    active = [start]
    rays = set()
    while active:
        ray = active.pop()
        loc, step = ray
        rays.add(ray)
        m = rows[loc[0]][loc[1]]
        next_rays = []
        if m == ".":
            next_rays.append(((loc[0] + step[0], loc[1] + step[1]), step))
        if m == "|":
            if step == (0, 1) or step == (0, -1):
                d = (1, 0)
                next_rays.append(((loc[0] + d[0], loc[1] + d[1]), d))
                d = (-1, 0)
                next_rays.append(((loc[0] + d[0], loc[1] + d[1]), d))
            else:
                next_rays.append(((loc[0] + step[0], loc[1] + step[1]), step))
        if m == "-":
            if step == (1, 0) or step == (-1, 0):
                d = (0, 1)
                next_rays.append(((loc[0] + d[0], loc[1] + d[1]), d))
                d = (0, -1)
                next_rays.append(((loc[0] + d[0], loc[1] + d[1]), d))
            else:
                next_rays.append(((loc[0] + step[0], loc[1] + step[1]), step))
        if m == "/":
            if step == (1, 0):
                d = (0, -1)
            if step == (0, 1):
                d = (-1, 0)
            if step == (-1, 0):
                d = (0, 1)
            if step == (0, -1):
                d = (1, 0)
            next_rays.append(((loc[0] + d[0], loc[1] + d[1]), d))
        if m == "\\":
            if step == (1, 0):
                d = (0, 1)
            if step == (0, 1):
                d = (1, 0)
            if step == (-1, 0):
                d = (0, -1)
            if step == (0, -1):
                d = (-1, 0)
            next_rays.append(((loc[0] + d[0], loc[1] + d[1]), d))

        for next_ray in next_rays:
            loc, step = next_ray
            if not 0 <= loc[0] < len(rows) or not 0 <= loc[1] < len(rows[0]):
                continue
            if (loc, step) in rays:
                continue
            active.append(next_ray)
    return rays


rays = get_all_rays(((0, 0), (0, 1)))

ans_1 = len(set([l for l, v in rays]))
print(f"Part 1: {ans_1}")

from_north = [((0, ci), (1, 0)) for ci in range(len(rows[0]))]
from_south = [((len(rows) - 1, ci), (-1, 0)) for ci in range(len(rows[0]))]
from_west = [((ri, 0), (0, 1)) for ri in range(len(rows))]
from_east = [((ri, len(rows[0]) - 1), (0, 1)) for ri in range(len(rows))]

count = 0
counts = []

for ray in from_north + from_south + from_east + from_west:
    rays = get_all_rays(ray)
    ans = len(set([l for l, v in rays]))
    counts.append(ans)

print(f"Part 2: {max(counts)}")
