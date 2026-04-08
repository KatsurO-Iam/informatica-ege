for a in range(1, 200):
    f = 1
    for x in range(1, 200):
        f *= (((x % 3 == 0) <= (x % 17 != 0)) or (a >= 190 - x))
    if f:
        print(a)