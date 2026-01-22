def f(a, h, ph):
    if a <= 35 or h > ph:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a - 2, h + 1, ph), f(a-4, h + 1, ph), f(a/2, h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)

for x in range(36, 1000):
    if not f(x, 0, 1) and f(x, 0, 3):
        print(x)
