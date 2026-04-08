from fnmatch import *
def f(n):
    s = set()
    a = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i % 10 == 7 and i != n:
                s.add(i)
            if (n//i) % 10 == 7 and (n//i) != n:
                s.add(n//i)
    return sorted(s)
k  = 0
for n in range(550_001, 10**7):
    t = f(n)
    if len(t) > 0:
        if len(t) == 3:
            print(n, max(t))
            k+=1
    if k == 5:
        break

# 550014 275007
# 550017 1567
# 550032 34377
# 550035 110007
# 550037 9017