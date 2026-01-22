def f(n):
    s = ''
    while n > 0:
        s += str(n%5)
        n = n//5
    return s[::-1]

for n in range(1, 1000):
    r = f(n)
    R = ''
    if len(r) % 2 == 0:
        beg, end = r[:(len(r)//2)], r[len(r)//2:]
        R = end + beg
    elif len(r) % 2 != 0:
        r += str(n%5)
        beg, end = r[:(len(r)//2)], r[len(r)//2:]
        R = end + beg
    if int(R,5) > 50:
        print(n)
        break
