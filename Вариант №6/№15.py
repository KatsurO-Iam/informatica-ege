c = 0
for a in range(1, 300):
    f = 1
    for x in range(1, 300):
        f *= (((x % 14 == 0) <= (x % 4 != 0)) or (x + a >= 200))
    if f == 1:
        print(a)