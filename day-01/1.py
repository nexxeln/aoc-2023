import re

r = 0

with open("in.txt") as f:
    lines = f.readlines()

    for line in lines:
        digits = re.findall(r"\d", line)

        r = r + int(digits[0] + digits[-1])

print(r)