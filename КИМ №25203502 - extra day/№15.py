for a in range(200):
    f = 1
    for x in range(1, 200):
        for y in range(1, 200):
            f *= ((x + y <= 27) or (y <= x - 1) or (y >= a))
    if f:
        print(a)