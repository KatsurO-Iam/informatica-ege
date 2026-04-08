def f(a,h,ph):
    if a >= 51:
        return h%2 == ph % 2
    if h == ph:
        return 0
    if a >= 31:
        comb = [f(a + 1, h + 1, ph), f(a + 2, h + 1, ph)]
    else:
        comb = [f(a + 1, h + 1, ph), f(a + 2, h + 1, ph), f(a * 2, h + 1, ph)]
    return any(comb) if (h + 1)%2 == ph % 2 else all(comb)

print(f(23, 0, 3))
print('--------------------19')
for x in range(1, 50):
    if not f(x,0, 2) and f(x, 0, 4):
        print(x)
print('--------------------20')
for x in range(1, 50):
    if not f(x,0,2) and not f(x,0,4)  and f(x,0,6):
        print(x)
print('--------------------21')
for x in range(1, 50):
    if not f(x, 0, 1) and f(x, 0, 3):
        print(x)
print('----------------------')