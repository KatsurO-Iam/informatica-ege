def f(a,b, h, ph):
    if a + b >= 103:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a+2, b, h + 1, ph), f(a*3, b, h+1, ph), f(a, b+2, h+1, ph), f(a, b*3, h+1, ph)]
    return any(comb) if (h + 1)% 2 == ph%2 else all(comb)

for x in range(1, 99):
    if (f(4, x, 0, 2) or f(4, x, 0, 4)) and not f(4,x,0,2):
        print(x)
