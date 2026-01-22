def f(a,h,ph):
    if a <= 65:
        return h%2==ph%2
    elif h == ph:
        return 0
    comb = [f(a-3, h + 1, ph), f(a - 5, h + 1, ph), f(a//4, h + 1, ph)]
    return any(comb) if ph % 2 == (h + 1) % 2 else all(comb)

for i in range(66, 200):
    if not f(i, 0,1) and f(i,0,2):
        print(i)
print('-------------------')
for i in range(66, 150):
    if not f(i, 0,1) and f(i,0,3):
        print(i)
print('-------------------')
for i in range(66, 150):
    if f(i, 0,2) or f(i,0,4):
        print(i)