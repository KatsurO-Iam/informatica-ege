import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return ((3*n +5) * f(n-1))

print(f(2073) /f(2070))