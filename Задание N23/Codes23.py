# def f(st, en, k):
#     if st > en or st == 27 or k > 15:
#         return 0
#     elif st == en:
#         return 1
#     else:
#         k+=1
#         return f(st + 2, en, k) + f(st * 3, en,k) + f(st**3, en,k)
#
# print(f(3,125,0))
from functools import lru_cache
from ipaddress import summarize_address_range

# def v(x): # функция, которая возвращает список делителей числа
#     d = set()
#     k = 0
#     for i in range(2,int(x**0.5)+1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     if len(d) > 0:
#         return sorted(d)
#9074
# def v(x):
#     s = []
#     for i in range(2, x):
#         if x % i == 0:
#             s.append(i)
#     return s
# def h(n1,n2):
#     d = v(n2)
#     for i in v(n1):
#         if i not in d:
#             continue
#         else:
#             return 0
#     return 1
# def f(start, end, p):
#     if p != 0:
#         if not h(p, start):
#             return 0
#     if start == end:
#         return 1
#     if start > end:
#         return 0
#     p = start
#     return f(start + 1, end, p) + f(start + 3, end, p) + f(start + 7, end, p)
# print(f(13, 31, 1))

from itertools import *
from sys import setrecursionlimit


# def suum(x):
#     s = 0
#     while x!=0:
#         s += x%10
#         x = x//10
#     return s
#
# s = [0] * 4097
# s[10] = 1
#
# for i in range(11, 4097):
#     s[i] += s[i-int(str(i)[-1])]
#     if i % int(str(i)[0]) == 0:
#         s[i] += s[i // int(str(i)[0])]
#
#     s[i] += s[(i//2) - suum(i)]
#
# print(s[4096])
from sys import setrecursionlimit
# setrecursionlimit(100_000_000)
# @lru_cache(maxsize = None)
# def a(n):
#     summ =0
#     while n != 0:
#         summ += n % 10
#         n = n // 10
#     return summ
# def b(n):
#     summ = 1
#     while n != 0:
#         summ *= n % 10
#         n = n // 10
#     return summ
#
# def f(s,e):
#     if s > e:
#         return 0
#     if s == e:
#         return 1
#     return f(a(s), e) + f(b(s), e)
#
# cnt = 0
# for i in range(1000):
#     p = f(i, 8)
#     if p != 0:
#         cnt +=1
# print(cnt)


# def f(s,e):
#     if s > e:
#         return 0
#     if s == e:
#         return 1
#     if s % 2 == 0:
#         return f(s + 1, e) + f(s + 2, e) + f(s * 2, e)
#     else:
#         return f(s*2, e)
#
# print(f(1,32))

def f(s,e):
    if s > e or s == 35:
        return 0
    elif s == e:
        return 1
    return f(s+1, e) + f(s+2, e) + f(s+4, e)

print(f(24, 33)*f(33,42))