def f(s, e):
    if s>e:
        return 0
    if s == e :
        return 1
    if s % 2 != 0:
        return f(s+1,e)+f(s+s+2,e)+f(s*2, e)
    elif s % 2 == 0:
        return f(s+1,e)+f(s+s+1,e)+f(s*2, e)

print(f(3,25)* f(25,75))