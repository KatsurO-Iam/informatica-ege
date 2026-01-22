c = 0
for a in range(1, 500):
    f = 1
    for x in range(1, 500):
        f *= (((x % 9 == 0) <= (x % 6 != 0)) or (x + a >= 100))
    if f == 1:
        print(a)