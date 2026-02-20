def f(a,h,ph):
    if a >= 22:
        return h%2 == ph % 2
    if h == ph:
        return 0
    comb = [f(a + 1, h + 1, ph), f(a + 2, h + 1, ph), f(a*2, h + 1, ph)]
    return any(comb) if (h + 1)%2 == ph % 2 else all(comb)


print('--------------------19')
for x in range(1, 21):
    if not f(x,0, 1) and f(x, 0, 2):
        print(x)
print('--------------------20')
for x in range(1, 21):
    if not f(x, 0, 1) and f(x, 0, 3):
        print(x)
print('--------------------21')
for x in range(1, 21):
    if f(x, 0, 2) or f(x, 0, 4) or f(x, 0, 6) or f(x, 0, 8) or f(x, 0, 10) or f(x, 0, 12):
        print(x)
print('----------------------')