def f(s,e):
    if s > e or s == 81:
        return 0
    if s == e:
        return 1
    return f(s + int(str(s)[0]), e) + f(s + 3, e) + f(s*2 - 1, e)

print(f(42, 73) * f(73, 89))