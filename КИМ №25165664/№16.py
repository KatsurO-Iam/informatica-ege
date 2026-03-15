import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)

def f(n):
    print('*')
    if n >= 1:
        print('*')
        f(n - 1)
        f(n - 2)
print(f(28))