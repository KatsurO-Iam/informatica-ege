minn = float('inf')
for n in range(1, 1000):
    r = bin(n)[2:]
    ssum = r.count('1')
    ost = ssum % 2
    r = r + str(ost)
    ssum = r.count('1')
    ost = ssum % 2
    r = r + str(ost)
    R = int(r, 2)
    if R > 198:
        if R < minn:
            minn = min(R, minn)

print(minn)

