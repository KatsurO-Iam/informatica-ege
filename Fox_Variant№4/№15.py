for a in range(1, 200):
    f = 1
    for x in range(1, 200):
        f *= (((x % 7 == 0) <= (x % 5 != 0)) or (x + a >= 80))
    if f:
        print(a)