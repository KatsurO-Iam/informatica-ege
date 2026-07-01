# def is_prime(n): # Функция проверки числа на простоту
# for i in range(2, int(n ** 0.5) + 1): # Перебираем возможные делители числа n
# if n % i == 0: # Если число n поделилось на i,
# return False # возвращаем ложь — оно не простое
# return n > 1 # Возвращаем истину, если число не является 1,
# #при этом цикл выше закончился
# def find_m(n): # Функция нахождения числа M
# min_d = max_d = 0
# for i in range(2, int(n ** 0.5) + 1): # Перебираем возможные делители числа n
# if n % i == 0: # Если число n поделилось на i, то проверяем основной делитель
# # и парный ему на простоту:
# if is_prime(i) and min_d == 0: # Если i — простое число,
# #при этом min_d ещё не найден,
# min_d = i # записываем его в качестве мин. простого делителя
# if is_prime(n // i) and max_d == 0: # Если n // i — простое число,
# 59
# %9a348e9666cb93f4244c0122fdb1c5bf%
# Образовательный проект «Школково» Информатика ЕГЭ, Основная волна
# # при этом max_d ещё не найден,
# max_d = n // i # записываем его в качестве макс. простого делителя
# if min_d > 0 and max_d > 0: # Если искомые делители нашлись,
# return min_d + max_d # возвращаем значение m
# return -1 # иначе возвращаем значение -1
#
#
#






# def f(n):
#     res = []
#     d = 2
#     while d <= int(n**0.5) + 1:
#         if n % d == 0:
#             n //= d
#             res.append(d)
#         d += 1
#     if n > 1:
#         res.append(n)
#     return res
#
# print(f(10))

# from fnmatch import *
#
def isp(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
#
#
# def f(n): #81
#     k = 0
#     s = set()
#     #print('------------------------')
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0 and i != n:
#             s.add(i)
#             s.add(n//i)
#             #print(i, n // i, k, ' del')
#             k += 1
#     return s
#
# def x(n):
#     s = 0
#     while n != 0:
#         s += n %10
#         n = n//10
#     return s
# for i in range(70240090, 10**10):
#    # t = x(i)
#     if fnmatch(str(i), '7?2*4??9.txt?') and i % 96437 == 0:
#         print(i)
#         break

# for i in range(10**10, 1702309, -2):
#     t = x(i)
#     z = 0
#     if fnmatch(str(i), '17*023?9.txt') and t % 11 == 0:
#         z += 1
#         print(i, t//11)
#     if z == 5:
#         break

    # if len(s)>6:
    #     return sorted(s, reverse= True)
# def a(n):
#     flag = True
#     for i in range(1, len(n)-1):
#         if not n[i] < n[i + 1]:
#             flag = False
#             break
#     return flag
# w = 0
# for i in range(500_000_000,0, -1): #84
#     t = f(i)
#     if t != None:
#         t = list(t)
#         if t[5] > 0:
#             maxx = t[5]
#             k = str(maxx)
#             #if t !=0:
#             if a(k):
#                 print(maxx, len(t))
#                 w+=1
#             if w ==5:
#                 break




# def is_prime(number): # функция для проверки простоты числа
#     if number == 1: return False
#     for div in range(2, int(number ** 0.5) + 1):
#         if number % div == 0:
#             return False
#     return True
#
#
# def f(x): # функция, которая возвращает список делителей числа
#     d = set()
#     k = 0
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return d
# print(f(100))
# #
#
# for i in range(228225, 531136):
#     k = 3
#     cnt = 0
#     maxx = 0
#     while k**3 <= i:
#         if i % k**3 == 0:
#             cnt +=1
#             maxx = k**3
#         k+=2
#     if cnt > 3:
#         print(cnt, maxx)



#
# def divs(x): # функция, которая возвращает список делителей числа
#     d = set()
#     for i in range(2,int(x**0.5)+1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     if len(d) > 0:
#         return sorted(d)
#
#
# for i in range(224466, 664422): Средняя Джобс.Е
#     p1 = i % 5 == 0 and i % 5 ** 2 != 0
#     p2 = i % 7 == 0 and i % 7 ** 2 != 0
#     p3 = i % 13 == 0 and i % 13 ** 2 != 0
#     if p1 + p2 + p3 == 3:
#         t = divs(i)
#         if max(t) < 100_000:
#             if max(t) % 100 == 19:
#                 print(i, max(t))



# def is_prime(number): #Сложная Джобс.Е
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# def f(n):
#     s = 0
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             if is_prime(i):
#                 s += i
#             elif is_prime(n // i):
#                 s += (n // i)
#     if s != 0:
#         return s
#     else:
#         return 1
# for i in range(33333, 55555):
#     t = f(i)
#     if i % t ==0:
#         if t > 250:
#             print(i, t)
#Сложнее ЕГЭ Джобс.Е
from time import *
# def is_prime(number):
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# start = time()
# def f(n):
#     k = 0
#     s = set()
#     #print('------------------------')
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             s.add(i)
#             s.add(n//i)
#             #print(i, n // i, k, ' del')
#             k += 1
#     return s

# kv = []
# sp = []
# for i in range(12621, 31196, 2000):
#     if not(is_prime(i)):
#         kv.append(i* i)
# #print(kv)
# for i in range(0, len(kv)):
#     print(kv[i], len(f(kv[i])))
#     # t = f(i) - 1
#     # if t > 1:
#     #     print(i, t)
#
# end = time()
# print(end - start)

# КЕГЭ - 5227
# def f(n):
#     s = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             s.add(i)
#             s.add(n//i)
#             return sorted(s)
#     return s
#
# for i in range(500_001, 501000):
#     x = str(i)
#     k = f(i)
#     t = sum(k)
#     if t % 10 == 9.txt:
#         print(i, t)
#
#
# def a(n):
#     if int(n**0.5)*int(n**0.5) == n:
#         return True
#     return False
# for i in range(1917, 10**10, 1917):
#     if f.fnmatch(str(i), '3&12&14*5') and i % 1917 == 0:
#         print(i, i/1917)

#
# for i in range(30120145, 10**10):
#     if i % 1917 == 0:
#         print(i)
#         break
# for i in range(30121821, 10**10, 1917):
#     if f.fnmatch(str(i), '3&12&14*5') and i % 1917 == 0:
#         print(i, i/1917)
#
# def d(n):
#     for i in n:
#         if i not in '02468':
#             return False
#     return True
# # for i in range(1021574, 10**10):
# #     if i % 2024 == 0:
# #         print(i)
# #         break
# cnt = 0
# maxx = []
#
# for i in range(700000, 10**6    , 42): #№ 18298 КЕГЭ
#     x = str(i)
#     # if f.fnmatch(x, '?1*23*92') and i % 7977 == 0:
#     #     #cnt +=1
#     #     #maxx.append(i)
#     #     print(i, i // 7977)
#
#     if f.fnmatch(x, '?2*4*0') and not f.fnmatch(x, '1*7*')  and i % 42 == 0:
#         cnt +=1
#         print(i, i//42)
#
# # print(cnt, max(maxx))
# for i in range(1200126, 10**8):
#    if i % 253 == 0:
#          print(i)
#          break
#
# for i in range(1200232, 10**8, 253):
#     k = str(i)
#     if f.fnmatch(k, '12??15*6') and i % 253 == 0:
#         print(i, i//253)

# for i in range(1200156, 100000000000):
#     if i % 253 == 0:
#         print(i)
#         break
# for i in range(1200232, 10 ** 8,253):
#     if f.fnmatch(str(i),'12??15*6') and i % 253==0:
#         print(i,i//253)

# def delt(n):
#     s = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             s.add(i)
#             s.add(n//i)
#     summ = sum([x for x in s])
#     return summ
# sp = []
# cnt = 0
# for i in range(136180, 10**7):
#     p = delt(i)
#     if p % 385 == 91:
#         print(p % 385)
#         sp.append([i,p])
#         cnt +=1
#     if cnt == 4:
#         break
# print(sp)

# def find_divisors(n):
#    divisors = 0
#    for i in range(2, n):
#        if n % i == 0:
#            divisors+=i
#    return divisors
# for i in range(136180,1000000):
#    a = find_divisors(i)
#    if a%385==91:
#        print(i,a)



# def deliteli(n):
#     sp = []
#     for i in range(1,n + 1):
#         if n%i == 0:
#             sp.append(i)
#     summary = 0
#     for i in sp:
#         summary+=i
#     return summary
# k = 0
# for i in range(500_001,1_000_000):
#     a = deliteli(i)
#     if str(a)[-1] == '6':
#         print(i,a)
#         k +=1
#     if k == 5:
#         break

# def delt(n):
#     s = set()
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             s.add(i)
#             s.add(n//i)
#     summ = sum([x for x in s])
#     return summ
# cnt = 0
# for i in range(500_001, 10**8):
#     k = delt(i)
#     if k % 10 == 6:
#         print(i, k)
#         cnt +=1
#     if cnt == 5:
#         break