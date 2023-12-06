with open(0) as f:
    lines = f.readlines()
    times = [int("".join(lines[0].split()[1::]))]
    distances = [int("".join(lines[1].split()[1::]))]
    ways = [sum(1 for hold in range(t) if hold * (t - hold) > d) for t, d in zip(times, distances)]
    r = 1
    for w in ways:
        r *= w

    print(r)