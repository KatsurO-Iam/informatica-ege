from  string import ascii_lowercase, digits


def f(n):
    s = ''
    while n > 0:
        s += str(n % 29)
        n = n // 29
    return s[::-1]

maxx = []
for x in range(1,8411):
    k = 29**293 + 29**271 - x
    cnt =0
    while k:
        if k % 29 == 0:
            cnt += 1
        k = k // 29
    maxx.append(cnt)
print(max(maxx))
#24