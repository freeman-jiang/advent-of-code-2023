with open("input.txt") as f:
    lines = f.read().splitlines()

res = 0

lines = [(x, 1) for x in lines]

for i, (line, count) in enumerate(lines):
    print(f'processing {count} copies of {line}')
    winning, mine = line.split(':')[1].split('|')
    winning, mine = winning.strip().split(), mine.strip().split()

    winning = set(int(x) for x in winning)
    mine = set(int(x) for x in mine)

    matching = len(winning.intersection(mine))
    if matching == 0:
        continue

    for _ in range(count):
        start = i + 1
        end = start + matching

        for j in range(start, end):
            if j >= len(lines):
                break
            lines[j] = (lines[j][0], lines[j][1] + 1)


print(sum(count for _, count in lines))
