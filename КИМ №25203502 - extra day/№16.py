import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1)*f(n-1)

print(((3*f(32_028) - f(32_027)))//f(32_026))