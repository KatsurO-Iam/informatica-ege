def f(n):
    s = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    s.add(n)
    return s

kub = set()
for j in range(3, 100, 2):
    kub.add(j**3)
kub = sorted(list(kub))
print(kub)
for i in range(228224, 531135+1):
    t = f(i)
    cnt = 0
    maxx = 0
    for x in t:
        if x in kub:
            cnt += 1
            maxx = max(maxx, x)
    if cnt > 4:
        print(cnt, maxx)
print(f(54))