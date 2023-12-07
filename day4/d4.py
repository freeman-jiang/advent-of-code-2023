with open("input.txt") as f:
    lines = f.read().splitlines()

res = 0

for line in lines:
    winning, mine = line.split(':')[1].split('|')

    winning, mine = winning.strip().split(), mine.strip().split()

    winning = [int(x) for x in winning]
    mine = [int(x) for x in mine]

    shared = sum([winning.count(x) for x in mine])

    if shared == 0:
        continue

    res += (2 ** (shared - 1))

print(res)
