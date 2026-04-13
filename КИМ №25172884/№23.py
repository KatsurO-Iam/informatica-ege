def f(s, e):
    if s>e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s+5,e)+f(s*2, e)

a = f(9,23)*f(23,35)
b = f(14,23)*f(23,35)
print(a+b)