import sys
from itertools import chain

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

sections = open(infile, "r").read().split("\n\n")

seeds = [int(c) for c in sections[0].split(" ")[1:]]

from_ranges_list = []
dest_starts_list = []

for s in sections[1:]:
    ranges = []
    starts = []
    for line in s.split("\n")[1:]:
        dest_start, from_start, rlen = [int(x) for x in line.split(" ")]
        starts.append(dest_start)
        ranges.append(range(from_start, from_start + rlen))
    dest_starts_list.append(starts)
    from_ranges_list.append(ranges)

### Part 1


def find_locations(seeds, total=None):
    locs = []
    for s_i, seed in enumerate(seeds):
        current = seed
        for sec_id, ranges in enumerate(from_ranges_list):
            for i in range(len(ranges)):
                r = ranges[i]
                s = dest_starts_list[sec_id][i]
                if current in r:
                    current = current - r.start + s
                    break
        locs.append(current)
        if total and (s_i % 100000) == 0:
            print(f"{s_i/total * 100} %")
    return locs


ans_1 = sorted(find_locations(seeds))[0]
print("Part 1:", ans_1)

#### Part 2


def range_splitter(org, splitter, offset):
    result = [], [org]
    new_offset = -splitter.start + offset
    if len(splitter) == 0:
        result = [], [org]
    elif org.start < splitter.start and splitter.stop < org.stop:
        result = [range(splitter.start + new_offset, splitter.stop + new_offset)], [
            range(org.start, splitter.start),
            range(splitter.stop, org.stop),
        ]
    elif splitter.start <= org.start and org.stop <= splitter.stop:
        result = [range(org.start + new_offset, org.stop + new_offset)], []
    elif org.start < splitter.start < org.stop:
        result = [range(splitter.start + new_offset, org.stop + new_offset)], [
            range(org.start, splitter.start)
        ]
    elif org.start < splitter.stop < org.stop:
        result = [range(org.start + new_offset, splitter.stop + new_offset)], [
            range(splitter.stop, org.stop)
        ]
    return result


def find_location_ranges(current_ranges, from_ranges_list, dest_starts_list):
    processed = []
    for current_range in current_ranges:
        todo = [current_range]
        for from_range, offset in zip(from_ranges_list[0], dest_starts_list[0]):
            rest_ranges = []
            for r in todo:
                converted, rest = range_splitter(r, from_range, offset)
                processed.extend(converted)
                rest_ranges.extend(rest)
            todo = rest_ranges
        processed.extend(rest_ranges)
    if len(from_ranges_list) <= 1:
        return processed
    else:
        return find_location_ranges(
            processed, from_ranges_list[1:], dest_starts_list[1:]
        )


# Part 1 again
start_ranges_1 = [range(x, x + 1) for x in seeds]
loc_ranges_1 = find_location_ranges(start_ranges_1, from_ranges_list, dest_starts_list)
ans_1 = sorted([r.start for r in loc_ranges_1])[0]
print("Part 1 again:", ans_1)

# Part 2
start_ranges_2 = [range(a, a + b) for a, b in zip(seeds[0::2], seeds[1::2])]
loc_ranges_2 = find_location_ranges(start_ranges_2, from_ranges_list, dest_starts_list)
ans_2 = sorted([r.start for r in loc_ranges_2])[0]
print("Part 2:", ans_2)
