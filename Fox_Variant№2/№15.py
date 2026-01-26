for a in range(300, 1, -1):
    f = 1
    for x in range(300, 1, -1):
        for y in range(300, 1, -1):
            f *= ((x % a != 0) <= ((x % 16 == 0) <= (x % 24 != 0)))
    if f:
        print(a)