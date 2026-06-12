for a in range(1, 4000):
    f = 1
    for x in range(1,4000):
        f *= ((x%a==0) or ((x>=1315 and x <= 1415) <= ((x % 191 !=0) or (x + a <= 4113))))
    if f:
        print(a)
    #2776