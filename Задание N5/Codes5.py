# minn = []
# for n in range(482, 1010):
#     r = str(oct(n)[2:])
#     s = 0
#     for k in r:
#         s += int(s)
#     if s % 2 == 0:
#         r = r + str(oct(s))[2:]
#     elif s % 2 !=0:
#         r = str(oct(s))[2:] + r
#     r = int(r,8)
#     minn.append(r)
# print(min(minn))
from itertools import count


# def f(n):
#     k = n.count('1')
#     return (k%2)
#
# minn = []
# for i in range(1,1000):
#     r = str(bin(i)[2:])
#     r1 = str(f(r))
#     r = r + r1
#     r2 = str(f(r))
#     r = r + r2
#     if int(r,2) > 77:
#         minn.append(i)
#
# print(min(minn))

# def f(n):
#     l = oct(n)[2:]
#     summ = 0
#     for s in l:
#         summ += int(s)
#     return summ
#
# minn = []
# for i in range(482,1200):
#     r = str(oct(i)[2:])
#     k = f(i)
#     if k % 2 == 0:
#         r1 = str(oct(k)[2:])
#         r = r + r1
#     elif k % 2 != 0:
#         r1 = str(oct(k)[2:])
#         r = r1 + r
#     R = int(r, 8)
#     minn.append(R)
#
# print(min(minn))

# def f(n):
#     l = ''
#     while n!=0:
#         l += str(n%7)
#         n = n//7
#     return l[::-1]
#
# maxx = []
# for i in range(1,1000):
#     r = f(i)
#     if i % 7 == 0:
#         r = r + r[-2:]
#     elif i % 7!=0:
#         a = (i % 7) * 2
#         d = f(a)
#         r = r + d
#     R = int(r, 7)
#     if R < 220:
#         maxx.append(i)


# for n in range(1,1000):
#     r = bin(n)[2:]
#     k = r
#     r = r + r[-1:]
#     if k.count('1')%2 == 0:
#         r = r + '0'
#     else:
#         r = r + '1'
#     r = r + '1'
#     if int(r,2) > 90:
#         print(n)

# for i in range(1,1000):
#     r = bin(i)[2:]
#     if i % 2 == 0:
#         r = '1' + r + '0'
#     elif i % 2 != 0:
#         r = '11' + r + '10'
#     R = int(r, 2)
#     summ = sum([int(x) for x in str(R)])
#     m = float('inf')
#     if summ > 17 and sum < m:
#         m = summ
#         print(bin(summ)[2:])


# def f(n):
#     s = ''
#     while n != 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
#
# for k in range(2, 100):
#     r = f(k)
#     if k % 3 == 0:
#         r = r + r[-2:]
#     elif k % 3 != 0:
#         x = (k % 3) * 3
#         r = r + f(x)
#
#     if int(r, 3) <= 150:
#         print(k)

for n in range(1000):
    r = bin(n)[2:]
    r += str(sum([int(x) for x in r]) % 2)
    r += str(sum([int(x) for x in r]) % 2)
    if int(r,2) > 198:
        print(r, int(r, 2))
        break

