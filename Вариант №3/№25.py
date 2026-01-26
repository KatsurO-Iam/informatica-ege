def check(n):
    s = str(n)
    return '1' in s or '3' in s
c = 0
num = 3000001
while c < 5:
    d = 2
    f = []
    temp = num
    while d * d <= temp:
        if temp % d == 0:
            while temp % d == 0:
                f.append(d)
                temp //= d
        d += 1
    if temp > 1:
        f.append(temp)
    if len(f) == 2:
        if check(f[0]) and check(f[1]):
            print(num, max(f))
            c += 1
    num += 1
#идея нагло украдена с решето эратосфена
# 3000001 3517
# 3000009 1000003
# 3000013 3881
# 3000023 230771
# 3000031 22901