import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

pipe_map = [[c for c in line.strip()] for line in open(infile)]

for ri, row in enumerate(pipe_map):
    for ci, c in enumerate(row):
        if c == "S":
            s_addr = ri, ci
            s_type = "S"

tile_io = {
    "|": (True, False, True, False),
    "-": (False, True, False, True),
    "L": (True, True, False, False),
    "J": (True, False, False, True),
    "7": (False, False, True, True),
    "F": (False, True, True, False),
    "S": (True, True, True, True),
    ".": (None, None, None, None),
}

current_addr = s_addr
current_type = s_type
prev_addr = None
count = 0

in_loop = [current_addr]

while True:
    for d_i, cand_dir in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
        cand_addr = current_addr[0] + cand_dir[0], current_addr[1] + cand_dir[1]
        if not cand_addr[0] in range(0, len(pipe_map)) or not cand_addr[1] in range(
            0, len(pipe_map[0])
        ):
            continue
        if not tile_io[current_type][d_i]:
            continue
        if cand_addr == prev_addr:
            continue
        cand_type = pipe_map[cand_addr[0]][cand_addr[1]]
        if tile_io[cand_type][(d_i + 2) % 4]:
            break
    count += 1
    in_loop.append(cand_addr)
    if cand_type == "S":
        break
    prev_addr = current_addr
    current_addr = cand_addr
    current_type = cand_type

ans_1 = int(count / 2)
print(f"Part 1: {ans_1}")
if infile == "input":
    assert ans_1 == 6823

### Part 2

# Replace "S"
pipe_map[s_addr[0]][s_addr[1]] = list(tile_io.keys())[
    list(tile_io.values()).index(
        (
            (s_addr[0] - 1, s_addr[1]) in in_loop,
            (s_addr[0], s_addr[1] + 1) in in_loop,
            (s_addr[0] + 1, s_addr[1]) in in_loop,
            (s_addr[0], s_addr[1] - 1) in in_loop,
        )
    )
]

# Topology inside search
count = 0
for ri in range(len(pipe_map)):
    inside = False
    entry_type = None
    for ci in range(0, len(row)):
        if (ri, ci) in in_loop:
            tile_type = pipe_map[ri][ci]
            if tile_type in ("F", "|", "L"):
                inside = not inside
                entry_type = tile_type
            elif tile_type == "7" and entry_type == "F":
                inside = not inside
            elif tile_type == "J" and entry_type == "L":
                inside = not inside
        else:
            count += inside

print(f"Part 2: {count}")
if infile == "input":
    assert count == 415
