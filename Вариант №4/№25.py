def check(n):
    s = str(n)
    return '1' in s or '2' in s
c = 0
num = 4000001
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
# 4000001 97561
# 4000006 2000003
# 4000013 210527
# 4000021 2221
# 4000027 2251