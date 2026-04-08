def f(s, e):
    if s>e:

        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s+2,e)+f(s*3, e)

a = f(6, 15)*f(15,21)*f(21,25)
b = f(6,15) * f(15, 25) - a
c = f(6, 21)*f(21, 25) - a
print(b + c)