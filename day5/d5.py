with open('input.txt') as f:
    lines = f.read().splitlines()

seeds = lines[0].split(':')[1].strip().split(' ')
seeds = [int(x) for x in seeds]


# Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
mappings: list[list[list[int]]] = []

lines = lines[2:]


for line in lines:
    if not line:
        continue
    if ':' in line:
        mappings.append([])
        continue
    lst: list[int] = []
    line = line.strip()
    dest_start, src_start, range_len = [int(x) for x in line.split(' ')]
    mappings[-1].append([dest_start, src_start, range_len])


def find_seed_location(seed: int):
    print(f'finding seed {seed}')
    current = seed

    for category in mappings:
        for m in category:
            dest_start, src_start, range_len = m
            # print(dest_start, src_start, range_len)

            dest_end = dest_start + range_len
            src_end = src_start + range_len
            # print(f'src start {src_start}, src end {src_end}')

            if src_start <= current < src_end:
                diff = current - src_start
                current = dest_start + diff
                break

    return current


part1 = min([find_seed_location(x) for x in seeds])
print(part1)
