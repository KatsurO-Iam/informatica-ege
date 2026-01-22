c = 0
for a in range(1, 100):
    f = 1
    for x in range(1, 100):
        for y in range(1, 100):
            f *= ((y > a) or (152 != 2*y + 3*x) or (a < x))
    if f:
        c +=1
print(c)
#30