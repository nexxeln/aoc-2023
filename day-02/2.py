with open(0) as f:
    r = []
    lines = f.readlines()
    total = 0

    for line in lines:
        name, c = line.strip().split(":")
        right = c.split(";")
        game = name.split(" ")[-1]
        min_dict = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }

        for i in right:
            color_dict = {
                "red": 0,
                "blue": 0,
                "green": 0,
            }
            for j in i.split(","):
                count, color = j.strip().split(" ")
                color_dict[color] = int(count)

            for k in color_dict:
                min_dict[k] = max(min_dict[k], color_dict[k])

        total += min_dict["red"] * min_dict["blue"] * min_dict["green"]


print(total)