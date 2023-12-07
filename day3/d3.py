

with open('input.txt') as f:
    m: list[list[str]] = []

    lines = f.read().splitlines()

    for row, l in enumerate(lines):
        m.append([])
        for j, c in enumerate(l):
            m[row].append(c)

    def is_symbol(row: int, col: int):
        if not (0 <= row < len(m) and 0 <= col < len(m[row])):
            return False

        c = m[row][col]

        return not c.isdigit() and c != "."

    def adjacent_to_symbol(row: int, start: int, end: int):
        top = row - 1
        bottom = row + 1
        left = start - 1
        right = end + 1

        # Check left and right
        if is_symbol(row, left) or is_symbol(row, right):
            return True

        # Check diagonals TL, BL, TR, BR
        if is_symbol(top, left) or is_symbol(bottom, left) or is_symbol(top, right) or is_symbol(bottom, right):
            return True

        # Check each of the digits top and bottom
        for col in range(start, end + 1):
            if is_symbol(top, col) or is_symbol(bottom, col):
                return True

        return False

    res = 0

    for row, r in enumerate(m):
        j = 0

        while j < len(r):
            if m[row][j].isdigit():
                # Get the maximum digit from the line that you can
                start = j

                while j < len(r) and m[row][j].isdigit():
                    j += 1

                num = int("".join(m[row][start:j]))

                # -1 because the last while loop iterations puts j at one past
                if adjacent_to_symbol(row, start, j - 1):
                    res += num

            j += 1

    print(res)
