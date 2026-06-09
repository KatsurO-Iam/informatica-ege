def f(s,e):
    if s < e or s == 7:
        return 0
    if s == e:
        return 1
    return f(s - 1,e) + f(s - 4, e) + f(s//3, e)

print(f(19,13)*f(13,2))