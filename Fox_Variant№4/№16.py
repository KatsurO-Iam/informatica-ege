from sys import setrecursionlimit

setrecursionlimit(1000000)

def f(n):
    if n == 1:
        return 2
    elif n > 1:
        return ((2*n)*f(n - 1))


print(f(2003)//f(2000))

# sp = [0]*3000
# for i in range(3000):
#     if i < 2:
#         sp[i] = 1
#     elif i > 1 and i % 2 == 0:
#         sp[i] = 2*i*sp[i - 1]
#     elif i > 1 and i % 2 != 1: