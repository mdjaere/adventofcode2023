import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
puzzles = [
    [l.strip() for l in p.split("\n")] for p in open(infile).read().split("\n\n")
]


def get_mirror_index(p, defects=0):
    mirrored = None
    for i in range(len(p)):
        if i < 1 or i > len(p) - 1:
            continue
        imperf = 0
        mirrored = True
        a = reversed(p[0:i])
        b = p[i:]
        for x, y in zip(a, b):
            for j in range(len(x)):
                if x[j] != y[j]:
                    imperf += 1
            if imperf > defects:
                mirrored = False
                break
        if imperf != defects:
            mirrored = False
        if mirrored:
            break
    return mirrored, i


def find_mirrors(puzzles, defects=0):
    score = 0

    for p in puzzles:
        mirrored = None
        mirrored, i = get_mirror_index(p, defects)
        if mirrored:
            score += i * 100
        else:
            mirrored, i = get_mirror_index(list(zip(*p)), defects)
            if mirrored:
                score += i
    return score


ans_1 = find_mirrors(puzzles, defects=0)
print("Part 1:", ans_1)
assert ans_1 == 35232


ans_2 = find_mirrors(puzzles, defects=1)
print("Part 2:", ans_2)
assert ans_2 == 37982
