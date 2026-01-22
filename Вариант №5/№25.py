def f(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    r = []
    for x in s:
        if x % 10 == 7 and x != 7 and x != n:
            r.append(x)
    return r
k = 0
for i in range(700001, 10**6):
    t = f(i)
    if len(t) != 0:
        print(i, min(t))
        k += 1
    if k == 5:
        break