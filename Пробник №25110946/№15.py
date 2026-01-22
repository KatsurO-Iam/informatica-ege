for a in range(1,1000):
    f = 1
    for x in range(1,1000):
        f *= ((x % a != 0) <= ((x % 28 == 0)<=(x % 49 != 0)))
    if f:
        print(a)