def f(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)

    return s
k = 0
for i in range(1_000_001, 2_000_001):
    t = f(i)
    if len(t) != 0:
        M = max(t)+min(t)
        if M % 10 == 6:
            print(i, M)
            k += 1
    if k == 5:
        break