from time import *
from functools import lru_cache


@lru_cache(maxsize= None)

def f(n):
    if n > 10_000:
        return 42
    if n <= 10000 and n % 2 ==0:
        return (2*n + f(n+3) + f(n + 4) + f(n+6))
    if n <= 10000 and n % 2 !=0:
        return (-(n+f(n+1) + f(n+3)))
st = time()
start = process_time()
print(f(9996) - f(9994))
en = time()

print(en - st)
print(start)