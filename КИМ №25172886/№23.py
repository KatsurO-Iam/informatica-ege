def f(s, e,cnt):
    if s>e:
        return 0

    if s == e :
        return 1 if len(cnt) > 50 else 0

    new_cnt = cnt.copy()
    if s != 2:
        new_cnt.add(s)
    return f(s+2,e, new_cnt)+f(s*3,e, new_cnt)+f(s*4, e, new_cnt)

print(f(2,400,(set())))