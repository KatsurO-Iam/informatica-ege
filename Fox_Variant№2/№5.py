s = []
for n in range(1000):
    r = bin(n)[2:]
    if n %2 != 0:
        r = r + '11'
    elif n % 2 == 0:
        r = r + '00'
    k = r.count('1')
    r = r +bin(k % 2)[2:]
    R = int(r,2)
    if R > 177:
        s.append(R)
print(min(s))