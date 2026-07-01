def f(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]

for x in range(1, 2030):
    a = 7**170 + 7**100 - x
    t = f(a)
    if t.count('0') == 70:
        print(x)