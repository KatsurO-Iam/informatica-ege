def f(n):
    s = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    return s
k = 0
for i in range(500_001, 10**7):
    t = f(i)
    if len(t) > 0:
        ss = sum(t)
    else:
        ss = 0
    if ss % 10 == 6:
        k +=1
        print(i, ss)
    if k == 5:
        break