def f(a, h, ph, e):
    if a >=29:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    if e == 0:
        comb = [f(a + 1, h + 1, ph, 1), f(a + 2, h + 1, ph, 2), f(a * 2, h + 1, ph, 3)]
        return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)
    elif e == 1:
        comb = [f(a + 2, h + 1, ph, 2), f(a * 2, h + 1, ph, 3)]
        return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)
    elif e == 2:
        comb = [f(a + 1, h + 1, ph, 1), f(a * 2, h + 1, ph, 3)]
        return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)
    elif e == 3:
        comb = [f(a + 1, h + 1, ph, 1), f(a + 2, h + 1, ph, 2)]
        return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)




for x in range(1, 29):
    if f(x, 0, 4, 0)  and not f(x, 0, 2, 0):
        print(x)