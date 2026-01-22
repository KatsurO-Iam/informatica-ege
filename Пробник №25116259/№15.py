for a in range(500):
    f = 1
    for x in range(500):
        for y in range(500):
            f *= (((x> 68) or (y > 89)) or (2*x - 7 * y < a))

    if f:
        print(a)
        break