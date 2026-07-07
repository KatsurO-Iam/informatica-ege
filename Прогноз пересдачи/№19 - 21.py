def f(a,b,h,ph):
    if a + b >= 154:
        return h % 2 == ph % 2
    if h == ph:
        return 0
    comb = [f(a +4, b, h + 1, ph), f(a,b + 4, h + 1, ph), f(a * 2, b,h+1,ph), f(a,b * 2, h + 1,ph)]
    return any(comb) if (h + 1)%2 == ph %2 else all(comb)

# for x in range(1,143):
#     if f(11, x, 0,2):
#         print(x) неудачный ход 36
#
for x in range(1,143):
    if not f(11, x,0,1) and f(11,x,0,3):
        print(x)

# for x in range(1,143):
#     if not f(11,x,0,2) and f(11,x,0,4):
#         print(x)