def f(a, h, ph):
    if a >= 110:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a + 1, h + 1, ph), f(a*2, h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)

print('--------------------19') # 308
for x in range(1, 109):
    if not f(x,0, 1) and f(x, 0, 2):
        print(x)
print('--------------------20') # 308 312
for x in range(1, 109):
    if not f(x, 0, 1) and f(x, 0, 3):
        print(x)
print('--------------------21') # 316
for x in range(1, 109):
    if not f(x, 0, 2) and f(x, 0, 4):
        print(x)
print('----------------------')
