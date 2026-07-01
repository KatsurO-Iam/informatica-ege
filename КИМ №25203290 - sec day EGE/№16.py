from sys import *

setrecursionlimit(10**9)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n-1)*f(n-1)

print((f(17258) + (3 *f(17257)))//f(17256))