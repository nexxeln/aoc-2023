with open(0) as f:
    lines = f.read().split("\n\n")
    maps = lines[1::]
    seeds = list(map(int, lines[0].split(":")[1].strip().split()))

    temp = seeds
    min_l = 0

    for m in maps:
        ranges = []

        for line in m.split("\n")[1::]:
            ranges.append(list(map(int, line.split())))
        # print(ranges)

        dest = []

        for s in temp:
            for x, y, z in ranges:
                if s in range(y, y + z):
                    dest.append(x + (s - y))
                    break
            else:
                dest.append(s)
    
        min_l = min(dest)
        temp = dest

print(min_l)