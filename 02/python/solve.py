infile = "input"
lines = [line.strip() for line in open(infile)]
games = [" ".join(line.split(" ")[2:]).split(";") for line in lines]
games = [[r.strip().split(", ") for r in g] for g in games]

list_1 = []
limit = {"red":12,"green":13,"blue":14}
list_2= []
for i, game in enumerate(games):
  above_limit = False
  max_count = {"red":0,"green":0,"blue":0}
  for samples in game:
    count = {"red":0,"green":0,"blue":0}
    for entry in samples:
      val, key = entry.split(" ")
      count[key] = int(val)
    for k,v in count.items():
      if v > limit[k]:
        above_limit = True
      max_count[k]=max(max_count[k],v)
  if not above_limit:
    list_1.append(i+1)
  game_power = 1
  for v in max_count.values():
    game_power *= v
  list_2.append(game_power)
ans_1 = sum(list_1)
ans_2 = sum(list_2)

print("Part 1", ans_1)
# if infile == "input":
#     print(ans_1 == 2239)
print("Part 2", ans_2)
# if infile == "input":
#     print(ans_2 == 83435)
