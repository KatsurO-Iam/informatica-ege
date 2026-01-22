# for x in range(1, 2030):
#     s = 7**170 + 7**100-x
#     r = ''
#     while s != 0:
#         r += str(s % 7)
#         s = s // 7
#     r = r[::-1]
#     if r.count('0') == 71:
#         print(x)

# from string import digits, ascii_letters
# k = digits + ascii_letters
# w = k[:12]
# print(len(k))
# a =0
# for x in w:
#     a = int(f'2AB{x}', 12)
#
# z = k[:17]
# for x in z:
#     t = int(f'{x}8E', 17)
#
# for i in range(1,1000):
#     r = bin(i)[2:]
#     if i % 2 == 0:
#         r = r+'10'
#     elif i % 2 != 0:
#       r = '1' + r + '00'
#     R = int(r, 2)
#     if R > 107:
#         print(i)
#         break
#
# def f(n):
#     s = ''
#     while n!=0:
#         s += str(n % 7)
#         n = n // 7
#     return s.count('0')
#
# r = 49**8+7**24 - 7
# k = f(r)
# print(k)

# def f(n):
#     k = ''
#     while n!=0:
#         k += str(n%7)
#         n = n//7
#     return k[::-1]
#
#
# s = 7 * 49**120 - 6 * 343**65 - 5*7**40
# R = f(s)
# print(R.count('6'))

from string import digits, ascii_letters
from itertools import *
# k = digits + ascii_letters
# sl = k[:25]
#
# def f(n):
#     a = ''
#     while n!=0:
#         a += str(n % 25)
#         n = n // 25
#     d = [int(c) for c in a]
#     return d[::-1]
# cnt = 0
# for x in range(1_000_000):
#     X = f(x)
#     s = 25**340 + 25**79 - 5**60 + X
#     ans = f(s)
#     if ans.count(0) == 287:
#         cnt +=1
# print(cnt)

# alp = (digits+ascii_letters)[:21]
# print(alp)
# for x in alp:
#     p = int(f'82934{x}2',21) + int(f'2924{x}{x}7',21) + int(f'67564{x}8',21)
#     if p % 20 == 0:
#         print(p//20)

# n = 2*2187**2020 + 792**2021 - 2 * 243**2022 + 81**2023 - 2*27**2024 - 6561
# c = 0
# while n > 0:
#     d = n % 27
#     if d > 9.txt:
#         c+=1
#     d = d//27
#
# print(c)

# alp = (digits+ascii_letters)[:29]
# print(alp)
# for x in alp:
#     p = int(f'923{x}874',29) + int(f'524{x}6152',29)
#     if p % 28 == 0:
#         print(x, p // 28)

def f(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]
m = 0
for x in range(1,1950):
    r = f(72070 + 7400 - x)
    m = max(m, r.count('0'))
print(m)

