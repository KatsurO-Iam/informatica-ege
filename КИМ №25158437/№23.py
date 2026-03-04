def f(s, e, k1, k2):
    if s>e:
        return 0
    if s == e:
        return 1
    if k1 == k2 == '1':
        return f(s*2,e,k2, '2')
    elif k1 == k2 == '2':
        return f(s+1,e,k2, '1')
    else:
        return f(s+1,e,k2, '1')+f(s*2,e,k2, '2')
print(f(1,16, '', ''))