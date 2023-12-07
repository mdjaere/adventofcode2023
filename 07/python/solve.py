import sys
from collections import Counter

infile = sys.argv[1] if len(sys.argv) > 1 else "input"


infile = "input"
lines = [line.strip() for line in open(infile)]

### Part 1

types = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 2, 2],
    [1, 1, 3],
    [2, 3],
    [1, 4],
    [5],
]

card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def get_type(hand):
    counted = sorted(Counter(hand).values())
    return types.index(counted)


hands = []

for line in lines:
    hand, score = [s.strip() for s in line.split(" ")]
    type = get_type(hand)
    conv_hand = str(type).zfill(2)
    for c in hand:
        conv_hand += str(card_values.index(c)).zfill(2)
    hands.append((conv_hand, score))

hands.sort(key=lambda x: x[0])

ans_1 = sum([int(x[1]) * (i + 1) for i, x in enumerate(hands)])
print("Part 1:", ans_1)

### Part 2

card_values_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def get_type_2(hand):
    count = Counter(hand)
    s_count = sorted(count.values())
    if count["J"] in [0, 5]:
        return types.index(s_count)
    if count["J"] == 1:
        if s_count == [1, 1, 1, 1, 1]:
            return types.index([1, 1, 1, 2])
        if s_count == [1, 1, 1, 2]:
            return types.index([1, 1, 3])
        if s_count == [1, 2, 2]:
            return types.index([2, 3])
        if s_count == [1, 1, 3]:
            return types.index([1, 4])
        if s_count == [1, 4]:
            return types.index([5])
    if count["J"] == 2:
        if s_count == [1, 1, 1, 2]:
            return types.index([1, 1, 3])
        if s_count == [1, 2, 2]:
            return types.index([1, 4])
        if s_count == [2, 3]:
            return types.index([5])
    if count["J"] == 3:
        if s_count == [1, 1, 3]:
            return types.index([1, 4])
        if s_count == [2, 3]:
            return types.index([5])
    if count["J"] == 4:
        return types.index([5])
    raise Exception("Escaped hand:", hand)


hands_2 = []

for line in lines:
    hand, score = [s.strip() for s in line.split(" ")]
    type = get_type_2(hand)
    conv_hand = str(type).zfill(2)
    for c in hand:
        conv_hand += str(card_values_2.index(c)).zfill(2)
    hands_2.append((conv_hand, score))

hands_2.sort(key=lambda x: x[0])

ans_2 = sum([int(x[1]) * (i + 1) for i, x in enumerate(hands_2)])
print("Part 2:", ans_2)
