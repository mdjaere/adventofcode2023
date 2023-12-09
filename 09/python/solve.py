import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

readings = [[int(x) for x in l.split()] for l in open(infile)]

def next_val(vals):
  diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
  if all(d == 0 for d in diffs):
    return vals[-1]
  return vals[-1] + next_val(diffs)

preds = []
for vals in readings:
  v = next_val(vals)
  preds.append(v)

ans_1 = sum(preds)
print("Part 1:", ans_1)

preds_2 = []
for vals in readings:
  v = next_val(vals[::-1])
  preds_2.append(v)

ans_2 = sum(preds_2)
print("Part 2:", ans_2)