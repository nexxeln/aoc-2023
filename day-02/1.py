with open(0) as f:
    r = []
    lines = f.readlines()
    total = 0

    for idx, line in enumerate(lines):
        name, c = line.strip().split(":")
        right = c.split(";")
        game = name.split(" ")[-1]

        for i in right:
            color_dict = {
                "red": 0,
                "blue": 0,
                "green": 0,
            }

            for j in i.split(","):
                count, color = j.strip().split(" ")
                color_dict[color] = int(count)

            if color_dict["red"] > 12 or color_dict["green"] > 13 or color_dict["blue"] > 14:
                continue
            else:
                total += idx + 1

print(total)





print(total)