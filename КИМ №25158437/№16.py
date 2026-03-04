import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n*f(n-1)
print(((f(2024)//4)+f(2023))//f(2022))