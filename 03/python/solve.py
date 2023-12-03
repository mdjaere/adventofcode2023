import sys
import re

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
rows = [line.strip() for line in open(infile)]

pattern = re.compile(r'\b\d+\b')
all_matches = [ list(pattern.finditer(row)) for row in rows  ]

def find_nums(ri, ci):
    nums = []
    for i in range(max(ri-1, 0), min(ri+2, len(rows)) ):
        for match in all_matches[i]:
            if match.start()-1 <= ci <= match.end():
                nums.append(int(match.group()))
    return nums

nums_1 = []
nums_2 = []

for ri, row in enumerate(rows):
    for ci, c in enumerate(row):
        if c != "." and not c.isdigit():
            nums = find_nums(ri, ci)
            nums_1 = nums_1 + nums
            if c == "*" and len(nums) == 2:
                nums_2.append( nums[0] * nums[1] )

ans_1 = sum(nums_1)
ans_2 = sum(nums_2)

print(f"Part 1: {ans_1}")
if infile == "input":
    assert(ans_1 == 536202)
    
print(f"Part 2: {ans_2}")
if infile == "input":
    assert(ans_2 == 78272573)
