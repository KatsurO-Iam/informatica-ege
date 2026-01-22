def f(a): #перерешать надо балбес
    s = ''
    while a > 0:
        s += str(a%3)
        a //= 3
    return s[::-1]
m = []
for n in range(1000):
    r = f(n)
    if n % 5 == 0:
        k = ''
        if len(r) > 3:
            k = f(int(r[-3:]))
        elif len(r) <= 3:
            k = r
        r = r + k
    elif n % 5 != 0:
        k = f((5 * (n % 5)))
        r = r + k
    R = int(r)
    if R < 5496:
        m.append(n)
print(max(m))