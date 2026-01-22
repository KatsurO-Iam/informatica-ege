def f(s, e  ):
    if s >   e:
        return 0
    if s == e:
        return 1
    k = f(s+1, e)
    if s % 3 != 0:
        k+=f(s+3, e)
    if s % 7 != 0:
        k+= f(s+7, e)
    return k

print(f(13,31))