
def initial_bag():
    return {
        'red': 12,
        'blue': 14,
        'green': 13
    }


def parse_line(l: str):
    game_id, games = l.split(":")
    game_id = int(game_id.split(" ")[1])

    games = games.strip()
    games = games.split(";")

    for g in games:
        rounds = g.split(",")
        for r in rounds:
            bag = initial_bag()
            r = r.strip()
            num, color = r.split(" ")
            num = int(num)

            bag[color] -= num

            if any([x < 0 for x in bag.values()]):
                return 0

    return game_id


with open("input.txt") as f:
    lines = f.read().splitlines()
    res = 0

    for line in lines:
        res += parse_line(line)

    print(res)
