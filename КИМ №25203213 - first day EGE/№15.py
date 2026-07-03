for a in range(1,500):
    f = 1
    for x in range(1, 500):
        f *= ((x % a == 0) or ((x >= 70 and x <=90) <= (x % 16 != 0)))
    if f:
        print(a)