def f(a,b,h,ph):
    if a == 0 or b == 0:
        return h % 2 == ph % 2
    can_move = (a >= 3 and b >= 3) or (a % 2 == 0) or (b % 2 == 0)

    if not can_move:
        return h % 2 == ph % 2

    if h == ph:
        return 0

    comb = []
    if a >= 3 and b >= 3:
        comb.append(f(a - 3, b - 3, h + 1, ph))
    if a % 2 == 0:
        comb.append(f(a // 2, a // 2, h + 1, ph))
    if b % 2 == 0:
        comb.append(f(b // 2, b // 2, h + 1, ph))

    return any(comb) if (h + 1) % 2 == ph else all(comb)

print(f(20,17,0,4))

print('--------------------19')
for x in range(6, 200):
    if not f(32,x, 0, 1) and f(32,x, 0, 2):
        print(x)
print('--------------------20')
for x in range(6, 200):
    if  f(32, x,0,1) or f(32, x, 0,3):
        print(x)
print('--------------------21')
for x in range(1, 200):
    if f(20, x, 0, 2) or f(20, x, 0, 4):
        print(x)
print('----------------------')

#решено руками