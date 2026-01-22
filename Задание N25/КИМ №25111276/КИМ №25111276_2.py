from fnmatch import *
def f(n):
    s = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    return list(s)

for i in range(1, 10**8):
    if fnmatch(str(i), '*15*7424'):
        t = f(i)
        p1 = 111 in t and 113 not in t and 127 not in t
        p2 = 111 not in t and 113 in t and 127 not in t
        p3 = 333 not in t and 333 not in t and 127 in t
        if p1 + p2 + p3 == 1:
            if p1:
                print(i, i // 111)
            if p2:
                print(i, i // 113)
            if p3:
                print(i, i // 127)