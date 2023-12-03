from turtle import numinput
from typing import Tuple

from networkx import number_of_selfloops

strdigits = ['one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']
strdigitsmap = {x: str(i) for i, x in enumerate(strdigits, 1)}


def first_digit(line: str):
    num_idx = float("inf")
    str_idxs: list[Tuple[int, str]] = []

    for i, c in enumerate(line):
        if c.isdigit():
            num_idx = i
            break

    for d in strdigits:
        i = line.find(d)
        if i == -1:
            continue

        str_idxs.append((i, d))

    if not str_idxs:
        return str(line[int(num_idx)])

    str_idx, digit = min(str_idxs)

    if num_idx < str_idx:
        return line[int(num_idx)]

    return strdigitsmap[digit]


def last_digit(line: str):
    num_idx = float("-inf")
    str_idxs: list[Tuple[int, str]] = []

    for i, c in reversed(list(enumerate(line))):
        if c.isdigit():
            num_idx = i
            break

    for d in strdigits:
        i = line.rfind(d)
        if i == -1:
            continue

        str_idxs.append((i, d))

    if not str_idxs:
        return str(line[int(num_idx)])

    str_idx, digit = max(str_idxs)

    if num_idx > str_idx:
        return line[int(num_idx)]

    return strdigitsmap[digit]


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

    res = 0

    for l in lines:
        first = first_digit(l)
        last = last_digit(l)

        num = int(first + last)
        res += num

    print(res)

# p1: 56397
