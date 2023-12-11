import sys
import itertools

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

lines = [line.strip() for line in open(infile)]

empty_rows = set(range(len(lines)))
empty_cols = set(range(len(lines[0])))
galaxies = set()
for ri, line in enumerate(lines):
    for ci, c in enumerate(line):
        if c == "#":
            galaxies.add((ri, ci))
            if ci in empty_cols:
                empty_cols.remove(ci)
            if ri in empty_rows:
                empty_rows.remove(ri)

pairs = list(itertools.combinations(galaxies, 2))


def get_distance_one_axis(pair, axis=0, void_size=1):
    v = sorted([pair[0][axis], pair[1][axis]])
    dist = v[1] - v[0]
    extra = sum(
        e in range(v[0], v[0] + dist) for e in (empty_rows, empty_cols)[axis]
    ) * (void_size - 1)
    return dist + extra


def get_space_distance(pairs, void_size=1):
    dists = 0
    for pair in pairs:
        dists += get_distance_one_axis(pair, axis=0, void_size=void_size)
        dists += get_distance_one_axis(pair, axis=1, void_size=void_size)
    return dists


ans_1 = get_space_distance(pairs, void_size=2)
print(f"Part 1: {ans_1}")

ans_2 = get_space_distance(pairs, void_size=10000000)
print(f"Part 2: {ans_2}")
