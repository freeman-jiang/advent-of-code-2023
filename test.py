s = "hello world"

for i, c in enumerate(s):
    if c == 'o':
        i += 3
        continue
    print(i, c)
