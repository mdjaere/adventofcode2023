import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

lines = [line.strip() for line in open(infile)]

winners = []
polled = []
for line in lines:
    win_raw, poll_raw = line.split(": ")[1].split("|")
    winners.append(set(int(x) for x in win_raw.strip().split(" ") if x))
    polled.append(set(int(x) for x in poll_raw.strip().split(" ") if x))
scores_1 = []
n_matches = []
for win, poll in zip(winners, polled):
    n_matching = len(set.intersection(win, poll))
    n_matches.append(n_matching)
    score = n_matching if n_matching <= 2 else pow(2, n_matching - 1)
    scores_1.append(score)

ans_1 = sum(scores_1)
if infile == "input":
    assert(ans_1 == 21158)
print("Part 1:", ans_1)

counts = [1] * len(lines)
for i, n_match in enumerate(n_matches):
    for j in range(n_match):
        next_card = i + j + 1
        if next_card >= len(counts):
            continue
        counts[next_card] += counts[i]

ans_2 = sum(counts)
if infile == "input":
    assert(ans_2 == 6050769)
print("Part 2:", ans_2)
