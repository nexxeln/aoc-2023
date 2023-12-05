with open(0) as f:
    lines = f.read().split("\n\n")
    maps = lines[1::]
    x = list(map(int, lines[0].split(":")[1].strip().split()))
    seeds = []

    for i in range(0, len(x), 2):
        seeds.append([x[i], x[i] + x[i + 1]])

    temp = seeds
    min_l = 0

for m in maps:
    ranges = []

    for line in m.split("\n")[1::]:
        ranges.append(list(map(int, line.split())))

    dest = []

    while len(temp) > 0:
        fst, lst = temp.pop()
        for x, y, z in ranges:
            f = max(fst, y)
            l = min(lst, y + z)
            if f < l:
                dest.append([f - y + x, l - y + x])
                if f > fst:
                    temp.append([fst, f])
                if lst > l:
                    temp.append([l, lst])
                break
        else:
            dest.append([fst, lst])

    min_l = min(dest)[0]
    temp = dest

print(min_l)