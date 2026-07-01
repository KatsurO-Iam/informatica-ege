def f(a,b,h,ph):
    if a + b >= 171:
        return h % 2 == ph % 2
    if h == ph:
        return 0
    comb = [f(a + 1, b , h + 1, ph), f(a, b + 1, h + 1, ph), f(a*2, b, h + 1, ph), f(a, b*2, h + 1, ph)]
    return any(comb) if (h + 1)%2 == ph % 2 else any(comb)

for x in range(1, 146):
    if f(25, x,0,2):
        print(x)
