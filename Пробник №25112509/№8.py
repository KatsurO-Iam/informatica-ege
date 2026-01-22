from functools import lru_cache


# @lru_cache(maxsize=None)
def f(x, y, k):
    if x > 10 and y > 10:
        return 0
    if x == 10 and y == 10:
        return 1
    return f(x, y - 1) + f(x + 1, y)

print(f(0,0))