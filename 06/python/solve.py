import sys
import re
from functools import reduce

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
lines = [line.strip() for line in open(infile)]

times = [int(x) for x in re.findall(r"[0-9]+", lines[0])]
distances = [int(x) for x in re.findall(r"[0-9]+", lines[1])]
races = list(zip(times, distances))

def get_winners(t, min_d):
    n_won = 0
    hold_t = 0
    won_last = False
    while True:
        speed = hold_t
        win = (speed * (t - hold_t)) > min_d
        if win:
            n_won += 1
        if won_last and not win:
            break
        won_last = win
        hold_t += 1
    return n_won

winners = []
for t, min_d in races:
    winners.append(get_winners(t, min_d))

ans_1 = 1
for x in winners:
    ans_1 *= x

print("Part 1:", ans_1)

t = int(reduce(lambda a, x: a + str(x), times, ""))
min_d = int(reduce(lambda a, x: a + str(x), distances, ""))

ans_2 = get_winners(t, min_d)
print("Part 2:", ans_2)
