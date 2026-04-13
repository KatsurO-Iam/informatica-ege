def f(n):
    s = ''
    while n > 0:
        s += str(n%4)
        n //= 4
    return s[::-1]
m = -float('inf')
for n in range(1,500):
    r = f(n)
    if r[0] == '3':
        r = r.replace('3', '*')
        r = r.replace('1', '3')
        r = r.replace('*', '1')
        r = '21' + r
    elif r[0] != '3':
        r = r + '12'
        r = '1' + r[1:]
    R = int(r, 4)
    if R < 598 and R > m:
        m = R
        print(n)

