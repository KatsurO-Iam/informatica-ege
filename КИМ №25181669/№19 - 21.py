def f(a,b,h,ph):
    if a + b >= 150:
        return h%2 == ph % 2
    if h == ph:
        return 0
    comb = [f(a + 1, b, h + 1, ph), f(a, b + 1, h + 1, ph), f(a + 2, b, h + 1, ph), f(a, b + 2, h + 1, ph), f(a+b, b, h + 1, ph), f(a, b + a, h + 1, ph)]
    return any(comb) if (h + 1)%2 == ph % 2 else all(comb)


print('--------------------19')
for x in range(1, 89):
    if not f(61, x,0, 1) and f(61, x, 0, 2):
        print(x)
print('--------------------20')
for x in range(1, 89):
    if not f(61, x, 0, 1) and f(61, x, 0, 3):
        print(x)
print('--------------------21')
for x in range(1, 89):
    if f(61, x, 0, 2) or f(61, x, 0, 4):
        print(x)
print('----------------------')