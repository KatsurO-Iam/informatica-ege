from math import ceil, floor


def f1(a, h, ph):
    if a <= 505:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a - 3, h + 1, ph), f(floor(a/5), h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph%2 else any(comb)

def f(a, h, ph):
    if a <= 505:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a - 3, h + 1, ph), f(floor(a/5), h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph%2 else all(comb)

print('--------------------19')
for x in range(100000, 505, -1):
    if not f1(x,0, 1) and f1(x, 0, 2):
        print(x)
        break
print('--------------------20')
k = 0
for x in range(505, 100000):
    if not f(x, 0, 1) and f(x, 0, 3):
        print(x)
        k +=1
    if k == 2:
        break
print('--------------------21')
for x in range(505, 100000):
    if not f(x, 0, 2) and f(x, 0, 4):
        print(x)
        break
print('---------------------#')

# --------------------19
# 12649
# --------------------20
# 2533
# 2534
# --------------------21
# 2536
# ---------------------#