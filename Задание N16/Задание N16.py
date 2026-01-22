from functools import lru_cache
lru_cache(maxsize=None)
from sys import setrecursionlimit, prefix

# s = [0] * 2030
# for i in range(1, 2030):
#     if i == 1:
#         s[i] = 1
#     if i > 1:
#         s[i] = i * s[i - 1]
#
# print(((s[2024]//4) +s[2023])//s[2022])


# s = [1] * 2030
# for i in range(2015, 2030):
#     if i >= 2025:
#         s[i] = i
#     if i < 2025:
#         s[i] = (i + 3 + s[i+3])
# print(s[2018]-s[2022])

#
# def f(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return (n+3 + f(n + 3))
#
# print(f(2018) - f(2022))

def f(n):
    if n == 0:
        return 0
    if n % 2 !=0:
        return f(n - 1) + 1
    if n % 2 == 0:
        return f(n//2)

cnt = 0
sp = [0] * 1_000_000_020
for i in range(len(sp)):
    if i == 0:
        sp[i] = 0
    if i % 2 != 0:
        sp[i] = sp[i-1] + 1
    if i % 2 == 0:
        sp[i] = sp[i//2]
    if sp[i] == 2:
        cnt +=1


# for i in range(1_000_000_000):
#     if sp[i] == 2:
#         cnt +=1

print(cnt)