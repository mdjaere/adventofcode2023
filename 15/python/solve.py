import sys
import re

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
codes = [s for s in open(infile).read().replace("\n", "").split(",")]


def hash_c(code):
    score = 0
    for c in code:
        score += ord(c)
        score *= 17
        score = score % 256
    return score


score = 0
for code in codes:
    score += hash_c(code)

print("Part 1:", score)
if infile == "input":
    assert score == 510013

boxes = [None] * 256
for code in codes:
    label = re.search(r"[a-z]+", code).group()
    box_id = hash_c(label)
    box = boxes[box_id]
    if box is None:
        box = []
    if code[-2] == "=":
        first = next(filter(lambda l: l[0] == label, box), None)
        lens = code.split("=")
        if first:
            i = box.index(first)
            box = box[:i] + [lens] + box[i + 1 :]
        else:
            box.append(lens)
    if code[-1] == "-":
        box = [l for l in box if l[0] != label]
    boxes[box_id] = box

score_2 = 0
for bi, box in enumerate(boxes, start=1):
    if box:
        for li, lens in enumerate(box, start=1):
            focal = bi * li * int(lens[1])
            score_2 += focal

print("Part 2:", score_2)
if infile == "input":
    assert score_2 == 268497
