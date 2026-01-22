from fnmatch import fnmatch

def f(n):
    s = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    if len(s) > 0:
        return sum(s)
    else:
        return 0


k = 0
for x in range(1, 10**7):
    p1 = x % 6 == 0
    p2 = x % 7 == 0
    p3 = x % 8 == 0
    if fnmatch(str(x), '?6*6*?6') and (p1 + p2 + p3 == 3):
        k += 1
        t = f(x)
        print(x, t)
    if k == 7:
        break