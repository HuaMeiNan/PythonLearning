def yanghui(t):
    if t == 1:
        print([1])

    if t != 1:
        print([1])
        line = [1, 1]
        print(line)
        for i in range(2, t):
            r = []
            for q in range(0, len(line) - 1):
                r.append(line[q] + line[q + 1])
            line = [1] + r + [1]
            yield line


for s in yanghui(4):
    print(s)