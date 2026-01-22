def ss(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return sorted(list(s))

a = range(7,27)
b = {11, 7}

for y in range(500):
    f = 1
    c = ss(y)
    if len(c) != 0:
        for x in range(500):
            f *= ((x in c) <= ((x in a) and (x not in b)))
        if f:
            print(y)


