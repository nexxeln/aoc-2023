import re

d = "one two three four five six seven eight nine".split()
r = 0

def convert(n):
    if n in d:
        return str(d.index(n) + 1)

    else :
        return n

with open("in.txt") as f:
    lines = f.readlines()

    for line in lines:
        digits = list(map(convert, re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)))
        r = r + int(digits[0] + digits[-1])

    print(r)


