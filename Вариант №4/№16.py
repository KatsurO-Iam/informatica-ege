from sys import setrecursionlimit
setrecursionlimit(1000000)

def f(n):
    if n < 10:
        return n
    if n >= 10:
        return (n**3 + f(n - 11))

print(f(900)- f(856))
#2760145884