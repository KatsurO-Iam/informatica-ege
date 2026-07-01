for n in range(1, 500):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    elif n % 2 != 0:
        r = '1' + r + '01'
    R = int(r, 2)
    if R >= 190:
        print(n)