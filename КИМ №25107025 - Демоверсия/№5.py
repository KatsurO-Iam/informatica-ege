for n in range(300):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    elif n % 3 != 0:
        r = r + bin((n % 3)*3)[2:]
    R = int(r, 2)
    if R >= 200:
        print(n)