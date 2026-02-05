from functools import lru_cache
from sys import setrecursionlimit

@lru_cache(maxsize=None)
def f(n):
    if n <= 2:
        return 1
    if n > 2 and n % 1 != 0:
        return f(n - 1) - n
    if n > 2 and n % 2 == 0:
        return f(n - 2) + g(n - 1) + 2
@lru_cache(maxsize=None)
def g(n):
    if n <= 0:
        return 2
    if n>0 and n % 2 != 0:
        return f(n-1)-2*g(n-2)
    if n % 2 == 0 and n > 0:
        return 2 * f(n-2) - 2*g(n - 1)

print(f(96))
