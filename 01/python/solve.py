import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"
lines = [line.strip() for line in open(infile)]

### Part 1

sum_1 = 0
for line in lines:
    digits = [x for x in line if x.isdigit()]
    sum_1 += int(digits[0] + digits[-1])

print("Part 1:", sum_1)
if infile == "input":
    print(sum_1 == 54990)

### Part 2

p = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sum_2 = 0

for line in lines:
    digits = []
    for i in range(len(line)):
        for key, value in p.items():
            if line[i:].startswith(key):
                digits.append(value)
                break
    sum_2 += int(digits[0] + digits[-1])

print("Part 2:", sum_2)
if infile == "example2":
    print(sum_2 == 281)
if infile == "input":
    print(sum_2 == 54473)
