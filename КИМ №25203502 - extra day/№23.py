def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    if str(s).count('1') >=1:
        return f(s + 1,e)+f(int(str(s).replace('1','3')), e)
    return f(s + 1, e)

print(f(10,84))