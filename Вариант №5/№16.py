from sys import setrecursionlimit
setrecursionlimit(1000000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n * f(n - 1))

print(((f(2025)//25) + f(2024))/f(2023))