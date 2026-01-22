def f(n):
    s = ''
    while n != 0:
        s += str(n % 9)
        n = n // 9
    return s


for x in range(1, 5769):
    a = 9**2025 + 9**1000 - x
    t = f(a)
    if t.count('0') == 1026:
        print(x)