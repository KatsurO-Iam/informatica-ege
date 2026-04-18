for a in range(1, 200):
    f = 1
    for x in range(1, 200):
        f *= (((x % 10 != 5) and (x % 10 == 4)) <= (x > a - 11))
    if f:
        print(a)

#руками