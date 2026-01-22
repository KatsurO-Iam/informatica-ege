for a in range(1, 500):
    f = 0
    for x in range(1,500):
        for y in range(1,500):
            f+= ((3*x+y > a) and (y < x) and (x < 30))
    if not f:
        print(a)
        break