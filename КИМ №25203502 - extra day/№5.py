m = float('inf')
for n in range(17,500):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    elif n % 2 != 0:
        r = '1' + r + '01'
    R = int(r, 2)
    m = min(m,R)
print(m)