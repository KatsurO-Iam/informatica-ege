def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    if '1' in str(s):
        return f(s+1,e) + f(int(str(s).replace('1', '2')), e)
    else:
        return f(s+1,e)

print(f(11,92))