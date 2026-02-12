def f(n):
    s = ''
    while n != 0:
        s += str(n % 5)
        n = n // 5
    return s


for x in range(2735,1,-1):
    a = 5**2025 + 5**1500 - x
    t = f(a)
    if t.count('0') == 527:
        print(x)