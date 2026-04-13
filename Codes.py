n = 4
r = bin(n)[2:]
if r.count('1') % 2 == 0:
    r = '1' + r[:-2] + '01'
elif r.count('1') % 2 != 0:
    r = '1' + r[2:] + '10'
print(r)
# n = 11
# r = bin(n)[2:]
# if n % 2 == 0:
#     r = r.replace('0', '1')
# if n % 2 != 0:
#     inx = r.find('1')
#     print(r[inx+1:])
#     r = '1' + r[inx+1:].replace('1', '00')
# print(r)

# def f(x, y, z, w):
#     return ((y == w) or (z <= w)) and (y == (x or z))
#
# from itertools import *
#
# for a1, a2, a3, a4 in product([0,1], repeat = 4):
#     table = [(0, 1, 1, 0), (a1, 1, 0, a2), (0, a3, a4, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, r))) for r in table] == [1,1,1]:
#                 print(*p, sep = '')
from string import digits, ascii_letters
from itertools import *
# k = digits + ascii_letters
# sl = k[:25]
#
# if isinstance(sl, int):
#     print(1)
# for a in range(50):
#     for b in range(50):
#         for c in range(50):
#             s = '>' + '1'* a + '2' * b + '3' * c
#             while '>1' in s or '>2' in s or '>3' in s:
#                 s = s.replace('>1', '21>3')
#                 s = s.replace('>2', '32>')
#                 s = s.replace('>3', '11>2')
#             if s.count('1') == 71 and s.count('2') == 54 and s.count('3') == 37:
#                 print(b)
#                 break
# from math import pi
# print((4*pi* 400 * 300**2)/2.54**2)
# print(70120488 * 24)
# print(1682891712/(8 * 1024 * 1024))
# print()
# from math import *
# from time import *
#
# def f(klast):
#     centroid, summ1 = None, float('inf')
#     for star in range(len(klast)):
#         summ = 0
#         for next_star in range(len(klast)):
#             if star == next_star:
#                 continue
#             x1, y1 = klast[star]
#             x2, y2 = klast[next_star]
#             summ += sqrt((x2-x1)**2 + (y2 - y1)**2)
#         if summ < summ1:
#             centroid = klast[star]
#             summ1 = summ
#     return centroid
#
#
# def centr(clust):
#     res = []
#     for point in clust:
#         res+= [(sum(dist(point, point1) for point1 in clust), point)]
#     return min(res)[1]

# file = open('27_A_4вар.txt')
# klasts = [[float(j) for j in i.replace(',', '.').split()] for i in file]
#
#
# klaster1 = [star for star in klasts if star[1] < 0]                                    ###
# klaster2 = [star for star in klasts if star[1] > 0]   ### 27A
#
# c1 = f(klaster1)
# c2 = f(klaster2)
#
# sr_x = (c1[0] + c2[0])/2
# sr_y = (c1[1] + c2[1])/2
#
# print(abs(int(sr_x * 10000)), abs(int(sr_y * 10000)))
# klasts = [tuple(map(float, points.replace(',', '.').split())) for points in open('27_A_4вар.txt')]
# clusters = []
#
# while klasts:
#     clusters.append([klasts.pop()])
#     for p1 in clusters[-1]:
#         neigh = [star for star in klasts if dist(p1, star) < 2]
#         clusters[-1] += neigh
#         for star in neigh:
#             klasts.remove(star)
# print(len(clusters), [len(cl) for cl in clusters])
#
# centroids = [centr(clas) for clas in clusters]
#
# l = len(centroids)
#
# x = sum([p[0] for p in centroids])/ l
# y = sum([p[1] for p in centroids])/ l
#
# print(abs(int(x * 10000)), abs(int(y * 10000)))


# print(int(abs(x * 10_000)), int(abs(y * 10_000)))
# def i(n):
#     flag = True
#     for i in range(1, len(n)-1):
#         if not n[i] < n[i + 1]:
#             flag = False
#             break
#     return flag
#
# print(i('123456789'))
# s = set()
# s.add(1)
# s.add(3)
# s.add(5)
# s.add(6)
# s.add(8)
# s = list(s)
# s = sorted(s, reverse= True)
# print(s[0] + s[1] + s[2])
# print(sorted(s, reverse= True))
# def f(x): # функция, которая возвращает список делителей числа
#     d = set()
#     k = 0
#     for i in range(2,int(x**0.5)+1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)

# t = f(54)
# print(t, " список")
# k = 0
# maxx = []
# for x in t:
#     if x % 2 != 0:
#         k+=1
#         maxx.append(x)
# print(k, max(maxx))
# def is_prime(number):
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# def f(n):
#     s = 0
#     k = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             # k.add(i)
#             # k.add(n//i)
#             if is_prime(i):
#                 s += i
#                 k.add(i)
#             elif is_prime(n // i):
#                 s += (n // i)
#                 k.add(n // i)
#     return s
#
#
# n = 38086
# print(f(n))
# # for x in kv:
# #     print(x, h(x))
#
#
#
# # # def f(n):
# #     r = ''
# #     while n!=0:
# #         r += str(n % 3)
# #         n = n//3
# #     return r[::-1]
# #
# # for n in range(1, 10000000):
# #     R = f(n)
# #     R = R.replace('2', "*")
# #     R = R.replace('0', '2')
# #     R = R.replace('*', '0')
# #     r = int(R, 3)
# #     if abs(n - r) == 1864648:
# #         print(n)
# #         break
#
#
# # import math
# # with open('a2.txt') as f:
# #     sp = [str(x) for x in f]
# #
# # m = int(sp[0])
# # f = []
# # for i in range(m):
# #     s = sp[i+1]
# # ip = '115.192.0.0'
# # print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
# # ip = '255.192.0.0 '
# # print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
# #
# #
# #
# # print(int('10111110', 2))
# #     s, p = list(s.split())
# #
# #     s = int(s)
# #     p = int(p)
# #
# #     a = (p + int(math.sqrt(p ** 2 - 16 * s))) // 4
# #     b = (p - int(math.sqrt(p ** 2 - 16 * s))) // 4
# #
# #     f.append(f'{a} {b}')
# #
# # with open('ans.txt', 'w') as wr:
# #     for i in f:
# #         wr.write(i)
# #
# #
#
# #
#
# #
# # ###для задания с ip
#
# # k = 6
# # cnt = 0
# # import itertools as t
# # l = list(t.product('10', repeat = 6))
# # for x in l:
# #     if (k + x.count('1')) % 5 != 0:
# #         cnt +=1
# # #
# # print(cnt)
# #
# # # #def f(sp):
#
#
#
# # a,b = map(int, input().split())
# # sp = [int(x) for x in input().split()]
# # # res = []
# # # for i in range(len(sp) - b):
# # #     res = [sp[i:i+b]]
# #
# # for i in range(a- b+1):
# #     s = sp[i: i + b]
# #     fl=0
# #     maxx = -float('inf')
# #     #print(s, '\n')
# #     for x in s:
# #         if s.count(x) == 1:
# #             fl+=1
# #             if x > maxx:
# #                 maxx = x
# #             # print(x, end = ' ')
# #     if fl==0:
# #         print('-1', end = ' ')
# #     else:
# #         print(maxx, end = ' ')
# #
# #
#
#
#
# # from os import write
# # def F(S, P):
# #     # Проверяем, является ли P четным числом
# #     if P % 2 != 0:
# #         return 0,0  # Периметр должен быть четным числом
# #
# #     half_perimeter = P // 2
# #
# #     # Перебираем возможные значения A от 1 до half_perimeter
# #     for A in range(1, half_perimeter):
# #         B = half_perimeter - A
# #         if A * B == S and A >= B:
# #             return A, B
# #
# #     return 0,0  # Если нет подходящих сторон
# #
# # with open('a2.txt') as f:
# #
# #     n = f[0]
# #     while n!=0:
# #         for i in range(1, (len(f)//2) + 1):
# #             s = f[i]
# #             p = f[i + 1]
# #             sides = F(s, p)
# #             a, b = sides
# #             file = open('ans.txt', 'w')
# #             write(a,b)
# #             n-=1
# # def find_rectangle_sides(S, P):
# #     # Проверяем, является ли P четным числом
# #     if P % 2 != 0:
# #         return None  # Периметр должен быть четным числом
# #
# #     half_perimeter = P // 2
# #
# #     # Перебираем возможные значения A от 1 до half_perimeter
# #     for A in range(1, half_perimeter + 1):
# #         B = half_perimeter - A
# #         if A * B == S and A >= B:
# #             return A, B
# #
# #     return None  # Если нет подходящих сторон
# #
# #
# # def main():
# #     input_filename = 'a2.txt'
# #     output_filename = 'ans.txt'
# #
# #     try:
# #         with open(input_filename, 'r') as file:
# #             lines = file.readlines()
# #
# #         if not lines:
# #             raise ValueError("Файл пустой.")
# #
# #         num_cases = int(lines[0].strip())
# #
# #         results = []
# #
# #         for i in range(1, num_cases + 1):
# #             if i >= len(lines):
# #                 raise ValueError(f"Не хватает данных для тестового случая {i}.")
# #
# #             S, P = map(int, lines[i].strip().split())
# #
# #             sides = find_rectangle_sides(S, P)
# #
# #             if sides:
# #                 A, B = sides
# #                 results.append(A,B, "\n")
# #             else:
# #                 results.append("Нет целочисленных сторон, удовлетворяющих условиям.\n")
# #
# #         with open(output_filename, 'w') as file:
# #             file.writelines(results)
# #
# #     except FileNotFoundError:
# #         print(f"Файл {input_filename} не найден.")
# #     except ValueError as e:
# #         print(f"Ошибка при чтении файла: {e}")
# #
# #
# # if __name__ == "__main__":
# #     main()
#
#
