def f(a):
    k = 0
    s = ''
    while  a > 0:
        s += str(a % 5)
        a //= 5
    return s.count('0')

m = 0
ans = 0
for x in range(1,2030):
    n = 5**150 + 5**100 - x
    t = f(n)
    if t >= m:
        m = t
        ans = x
print(ans)