from math import ceil

def f(a,h,ph):
    if a <= 49:
        return h%2 == ph % 2
    if h == ph:
        return 0
    comb = [f(a - 2, h + 1, ph), f(a - 5, h + 1, ph), f(int(a/3), h + 1, ph)]
    return any(comb) if (h + 1)%2 == ph % 2 else all(comb)


print('--------------------19')
for x in range(50, 1000):
    if not f(x,0, 1) and f(x, 0, 2):
        print(x)
print('--------------------20')
for x in range(50, 1000):
    if not f(x, 0, 1) and f(x, 0, 3):
        print(x)
print('--------------------21')
for x in range(50, 1000):
    if not f(x, 0, 2) and f(x, 0, 4):
        print(x)
print('----------------------')