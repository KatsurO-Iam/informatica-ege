b = range(132, 151)
for a in range(2,1000):
    f = 1
    for x in range(2, 1000):
        f *= (((x % a != 0) and (x >= 132 and x <= 150)) <= (x % 13 != 0))
    if f:
        print(a)
        break
