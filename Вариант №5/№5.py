for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r.replace('1', '11')
    elif n % 2 != 0:
        r = r.replace('0', '00')
    R = int(r, 2)
    if R > 70:
        print(n)