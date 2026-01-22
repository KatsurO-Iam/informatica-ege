for n in range(100):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    elif n % 3 != 0:
        k = (((n % 3) + 1) * 3)
        r = r + bin(k)[2:]
    R = int(r,2)
    if R <= 416:
        print(R)
