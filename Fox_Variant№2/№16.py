from sys import setrecursionlimit

setrecursionlimit(1000000)

def f(n):
    if n < 2:
        return 1
    elif n > 1 and n % 2 == 0:
        return ((2*n)*f(n - 1))
    elif n % 2 != 0 and n > 1:
        return (f(n-1) - 1)

print(f(2903)//f(2900))

# sp = [0]*3000
# for i in range(3000):
#     if i < 2:
#         sp[i] = 1
#     elif i > 1 and i % 2 == 0:
#         sp[i] = 2*i*sp[i - 1]
#     elif i > 1 and i % 2 != 1: