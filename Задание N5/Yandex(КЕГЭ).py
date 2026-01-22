for n in range(1, 1010):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[:-2]
    elif n % 3 != 0:
        k = (n % 3) * 3
        k = bin(k)[2:]
        r = r + k
    if int(r, 2) >= 195:
        print(int(r,2))
