for a in range(55, 200):
    f = 1
    for x in range(50, a):
        for y in range(5, a):
            f *= ((201 != y + 2*x) or (a > x) or (a > y))
    if f:
        print(a)
#68