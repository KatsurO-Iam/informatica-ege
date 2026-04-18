m = -float('inf')
for n in range(1,500):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r[:-2] + '01'
    elif r.count('1') % 2 != 0:
        r = '1' + r[2:] + '10'
    R = int(r, 2)
    if R > m and R < 100:
        m = R
        print(R)