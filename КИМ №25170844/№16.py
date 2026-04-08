import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)


def f(n):
    if n <= 10:
        return n
    if n >=10_000:
        return 1
    if n % 2 == 0 and 10 < n < 10_000:
        return ((n % 10) + f(n + 2))
    if n % 2 !=0 and 10 < n < 10_000:
        return (f(n-2) - ((n-1)%10))

print(f(4500)+f(5515))