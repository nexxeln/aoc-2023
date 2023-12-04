import re

r = 0

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]
    for line in lines:
        left, right = line.split("|")
        left_nums = re.findall(r"\d+", left)[1::]
        right_nums = re.findall(r"\d+", right)

        common = set(left_nums).intersection(right_nums)

        if len(common) > 0:
            r += 2 ** (len(common) - 1)

print(r)
