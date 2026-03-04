for a in range(50, 101):
    f = 1
    for x in range(1, 200):
        f *= ((x & a == 0) <= ((x & 31 != 0) <= (x & 35 != 0)))
    if f:
        print(a)