def f(n):
    s = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    return s
print(f(452021))
k = 0
for i in range(452022, 10**7):
    t = f(i)
    if len(t) > 0:
        m = min(t) + max(t)
    else:
        m = 0
    if m % 7 == 3:
        print(i, m)
        k+=1
    if k == 5:
        break