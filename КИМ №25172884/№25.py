from fnmatch import *
from math import *
def f(n):
    s = set()
    a = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)
k  = 0
for n in range(1, int(sqrt(10**7)) + 1):
    t = f(n*n)
    if len(t) > 0:
        if len(t) % 2 != 0 and fnmatch(str(n*n), '3*52?'):
            print(n*n, max(t))
