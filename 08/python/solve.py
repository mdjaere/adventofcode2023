import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

raw = open(infile).read()

rinst, rtiles = raw.split("\n\n")

instructions = [c == "R" for c in rinst.strip()]
l = len(instructions)
tiles = {}
for tile in rtiles.split("\n"):
    id, rest = tile.split(" = ")
    next_tiles = (rest[1:4], rest[6:9])
    tiles[id] = next_tiles


def steps_to_next(start_tile, test, offset=0):
    count = offset
    current_tile = start_tile
    while True:
        current_tile = tiles[current_tile][instructions[count % l]]
        count += 1
        if test(current_tile):
            return count, current_tile

steps, tile = steps_to_next("AAA", lambda x: x == "ZZZ")
print("Part 1:", steps)

tile_list = [k for k in tiles if k[2] == "A"]

def z_test(x):
    return x[2] == "Z"

rounds = []
for tile in tile_list:
    steps, tile_found = steps_to_next(tile, z_test, offset=0)
    rounds.append(int(steps/l))

x = 1
for r in rounds:
    x *= r
ans_2 = x * l
print("Part 2:", ans_2)