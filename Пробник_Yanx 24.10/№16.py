from sys import setrecursionlimit
setrecursionlimit(100000)
def f(n):
    if n == 41:
        return 41
    elif n > 41  and n % 2 == 0:
        return (f(n - 1) - n)
    else:
        return (n*f(n -2))

print(f(9094)//f(9089))