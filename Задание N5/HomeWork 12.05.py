def f(n):
    s = ''
    while n != 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]

for i in range(1,1000):
    r = f(i)
    if i % 25 == 0:
        r = r[-3:] + r
    elif i % 25 != 0:
        k = i % 25
        r = r + f(k)
    R = int(r,5)
    if R > 10_000:
        print(i, R)

