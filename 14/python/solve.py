import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip() for line in open(infile)]

R = len(lines)
C = len(lines[0])


def tilt(d, rows):
    if d == "cw":
        rows = ["".join(r) for r in zip(*rows)]
    if d == None:
        rows = rows
    if d == "ccw":
        rows = ["".join(r) for r in zip(*[reversed(r) for r in rows])]

    new_rows = []

    for ri, row in enumerate(rows):
        next_free = 0
        new_row = row
        for ci, c in enumerate(row):
            if c == "#":
                next_free = ci + 1
            elif c == "O":
                if ci > next_free:
                    new_row = (
                        new_row[0:next_free]
                        + "O"
                        + new_row[next_free + 1 : ci]
                        + "."
                        + new_row[ci + 1 :]
                    )
                next_free += 1
        new_rows.append(new_row)
    return new_rows


def calc_score(rows):
    score = 0
    for ri in range(len(rows)):
        for ci in range(len(rows[0])):
            if rows[ri][ci] == "O":
                multiplier = len(rows) - ci
                score += multiplier
    return score


history = {}


def full_round(rows, first=False):
    new_r = rows
    if first:
        new_r = tilt("cw", rows)
    else:
        new_r = tilt("ccw", new_r)
    new_r = tilt("ccw", new_r)
    new_r = tilt("ccw", new_r)
    new_r = tilt("ccw", new_r)
    return new_r


new_rows = tilt("cw", [line for line in lines])
print("Part 1:", calc_score(new_rows))

base = 0
freq_1 = 0
scores = []

for i in range(1000):
    if i == 0:
        new_rows = full_round(lines, first=True)
    else:
        new_rows = full_round(new_rows)
    s = hash(str(new_rows))
    if s not in history:
        history[s] = []
    history[s].append((i))
    if base == 0 and len(history[s]) == 2:
        base = i
    if base:
        score = calc_score(["".join(r) for r in zip(*new_rows)])
        scores.append(score)
    if freq_1 == 0 and len(history[s]) == 3:
        freq_1 = i - base
        break

quotient, remainder = divmod(1000000000 - base, freq_1)
ans_2 = scores[remainder - 1]
print("Part 2:", ans_2)



