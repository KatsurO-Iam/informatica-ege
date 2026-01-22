from fnmatch import *
def f(n):
    s = set()
    for i in range(1, int(n**0.5)):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    s.remove(n)
    return max(s)

for i in range(1, 10**6):
    if i % 23 == 0:
        t = f(i)
        if fnmatch(str(t), '*6215'):
            print(i, t)