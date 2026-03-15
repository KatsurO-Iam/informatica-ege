def f(a, b, h, ph):
    if a + b >= 212:
        return h%2 == ph % 2
    if h == ph:
        return 0
    comb = [f(a + b, b, h + 1, ph), f(a, a + b, h + 1, ph)]
    return any(comb) if (h + 1)%2 == ph % 2 else all(comb)


print('--------------------19')
for x in range(0, 111):
    if not f(100, x, 0, 1):
        print(x)
print('--------------------20')
for x in range(0, 111):
    if not f(50, x, 0, 1) and f(50, x, 0, 3):
        print(x)
        print(f(50, x, 0, 3))
print('--------------------21')
for x in range(0, 111):
    if f(10, x, 0, 4) or not f(10, x, 0, 3):
        print(x)
print('----------------------')