def f(n):
    ss = ''
    while n > 0:
        ss += str(n % 7)
        n = n // 7
    return ss[::-1]
maxx = 0
for x in range(2030):
    s = 7**170 + 7**100 - x
    s = f(s)
    if s.count('0') == 71:
        if maxx < x:
            maxx = max(maxx, x)

print(maxx)