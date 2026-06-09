from fnmatch import *

def f(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(list(s))

print(f(20))
k = 0
for i in range(800_001, 10**6):
    t = f(i)
    if len(t) != 0:
        m = max(t) + min(t)
        if m % 10 == 4:
            print(i, m)
            k +=1
    if k == 5:
        break

# for i in range(1917, 10**10, 1917):
#     if fnmatch(str(i), '3?12?14*5') and i % 1917 == 0:
#         print(i, i // 1917)