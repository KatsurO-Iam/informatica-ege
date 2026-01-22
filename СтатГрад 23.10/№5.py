minn = float('inf')
for n in range(1,1000):
    r = bin(n)[2:]
    if n % 5 == 0:
        r = r + '11'
    elif n % 5 != 0:
        k = bin(n //5)[2:]
        r = r + k
    R = int(r, 2)
    if R >= 783:
        minn = min(n, minn)
print(minn)
#49