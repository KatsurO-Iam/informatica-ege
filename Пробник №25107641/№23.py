from functools import lru_cache
@lru_cache(maxsize=None)
def f(s, e):
    if s < e or s == 15:
        return 0
    elif s == e:
        return 1
    return f(s-2,e) + f(s - 3, e) + f(s//3, e)

print(f(48, 25)*f(25, 17)*f(17, 4))