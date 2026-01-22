def f(n):
    s = ''
    while n > 0:
        s += str(n%3)
        n //= 3
    return s[::-1]
m = []
for n in range(1000):
    r = f(n)
    ss = sum([int(x) for x in r])
    if ss % 3 == 0:
        r = r + '212'
    elif ss % 3 != 0:
        k = f(ss * 2)
        r = r + k
    R = int(r, 3)
    if R > 490:
        m.append(R)
print(min(m))