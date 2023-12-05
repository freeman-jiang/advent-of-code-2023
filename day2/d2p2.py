
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

    max_bag = {x: 0 for x in initial_bag()}

    for g in games:

        rounds = g.split(",")
        for r in rounds:
            r = r.strip()
            num, color = r.split(" ")
            num = int(num)
            max_bag[color] = max(num, max_bag[color])

    product = 1
    for v in max_bag.values():
        product *= v

    return product


with open("input.txt") as f:
    lines = f.read().splitlines()
    res = 0

    for line in lines:
        res += parse_line(line)

    print(res)
