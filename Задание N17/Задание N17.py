# with open ('17_17873.txt') as f:
#     sp = [int(x) for x in f]
#
# minn = min(sp)
# maxx = []
# cnt = 0
# for i in range(len(sp) - 1):
#     p1 = sp[i] % 16 == minn
#     p2 = sp[i + 1] % 16 == minn
#     if(p1 + p2) >=1:
#         cnt+=1
#         maxx.append(sp[i] + sp[i+1])
#
# maxim = max(maxx)
# print(cnt, maxim)
#
# with open('17_19486.txt') as f:
#     sp = [int(x) for x in f]
#
# countt = 0
# for x in sp:
#     if x % 10 == 7:
#         countt += 1
# maxx = []
# cnt = 0
# for i in range(len(sp) - 1):
#     p1 = sp[i] < 0
#     p2 = sp[i+1] < 0
#     if (p1 + p2) == 1:
#         if sp[i] + sp[i+1] < countt:
#             maxx.append(sp[i] + sp[i + 1])
#             cnt +=1
# maxim = max(maxx)
# print(cnt, maxim)

# with open('17_5758.txt') as f:   // решал Леша
#     sp = [int(x) for x in f]
#
# moda = -1000000
# for i in sp:
#     if sp.count(i) > moda:
#         moda = i
# counter = 0
# maxxx = -1000000000000
# for i in range(len(sp) - 1):
#     for j in range(i + 1, len(sp)):
#         if ((sp[i] < moda < sp[j]) and (j-i)%2!=0) \
#                 or ((sp[j] < moda < sp[i]) and (i-j)%2!=0):
#             counter +=1
#             maxxx = max(maxxx, moda-sp[i],moda-sp[j])
# print(counter,maxxx)

# with open('17-399.txt') as f:
#     sp = [int(x) for x in f]
#
# minn = min([x for x in sp if (len(str(x)) == 3 and x // 100 == 5)])
# cnt = 0
# maxx = []
# for i in range(len(sp) - 1):
#     p1 = abs(sp[i]) % 10 == 4
#     p2 = abs(sp[i + 1]) % 10 == 4
#     p3 = (sp[i] + sp[i + 1]) % minn != 0
#     if p1 + p2 == 1 and p3 == 1:
#         cnt+=1
#         maxx.append(sp[i] + sp[i + 1])
#
# print(cnt, max(maxx))
# 1795 199007 - правильно

# with open('17-382.txt') as f:
#     sp = [int(x) for x in f]
#
# minn = min([x for x in sp if (len(str(x)) == 3 and x % 100 == 11)])
# cnt = 0
# maxx = []
# for i in range(len(sp) - 1):
#     p1 = len(str(sp[i])) != 3
#     p2 = len(str(sp[i + 1])) != 3
#     p3 = abs(sp[i] - sp[i + 1]) % minn == 0
#
#     if(p1 + p2 == 1 and p3 == 1):
#         cnt += 1
#         maxx.append(sp[i] + sp[i + 1])
# print(cnt, max(maxx))
# 8 8089 - правильно



# 262
# with open('17-257.txt') as f:
#     sp = [int(x) for x in f]
#
# maxx = max([x for x in sp if x % 2 != 0])
# minn = min([x for x in sp if x % 2 != 0])
# mimax = minn + maxx
# cnt = 0
# s = []
# for i in range(len(sp) - 1):
#     p1 = (sp[i] + sp[i + 1]) % 2 == 0 and  (sp[i] + sp[i + 1])>mimax
#     if p1:
#         s.append(sp[i] + sp[i + 1])
#         cnt+=1
#
# print(cnt, min(s))
# 250 10094

# 248
# with open('17-257.txt') as f:
#      sp = [int(x) for x in f]
#
# maxx = max([x for x in sp if x % 119 == 0])
# cnt = 0
# m = []
# for i in range(len(sp) - 1):
#     p1 = sp[i] > maxx
#     p2 = sp[i + 1] > maxx
#
#     q1 = sp[i] % 100 == 21
#     q2 = sp[i + 1] % 100 == 21
#     if (p1 + p2 == 1) and (q1 + q2 == 1):
#         cnt += 1
#         m.append(sp[i] + sp[i + 1])
#
# print(cnt, min(m)) - неправильно

# minn = min([x for x in sp if x > 0 and x % 2025 == 0])
# print((minn))
#
# cnt = 0
# mini = []
#
# for i in range(len(sp) - 3):
#     p1 = sp[i] > 0
#     # p2 = sp[i + 1] < 0
#     # p3 = sp[i + 2] < 0
#     p4 = sp[i + 3] > 0
#
#     q1 = abs(sp[i + 1] - sp[i + 2]) <= minn
#     if (p1  + p4) == 2 and q1 == 1:
#         cnt +=1
#         mini.append(sp[i] + sp[i + 1] + sp[i + 2] + sp[i + 3])
#
# print(cnt, min(mini))

# cout = 0
# for x in sp:
#     if abs(x) < 100:
#         cout += 1
# cnt = 0
# maxi = []
# for i in range(len(sp) - 1):
#     sr = (sp[i] + sp[i+1]) / 2
#     if sr > cout:
#         cnt +=1
#         maxi.append(sp[i] + sp[i + 1])
#
# print(cnt, max(maxi))

# import fnmatch as t
#
# with open('17-363.txt') as f:
#     sp = [int(x) for x in f]
#
#
# cnt = 0
# for i in range(12300, 10 ** 6):
#     if t.fnmatch(str(i), '?2*3?5'):
#         cnt += 1
#
# print(cnt)
#
# #
# summ = sum([x for x in sp])
# arif = summ/len(sp)
#
# maix = []
# cnt = 0
# for i in range(2, len(sp) - 2):
#     pr = sp[i] + sp[i + 1]
#     pr2 = sp[i - 1] + sp[i + 2]
#     if (pr > pr2):
#         maix.append(sp[i] + sp[i + 1])
#         p1 = sp[i]  > arif
#         p2 = sp[i + 1] > arif
#         if (p1 + p2) >= 1:
#             cnt +=1
#
# print(max(maix), cnt)
#
# with open('17-328.txt') as f:
#   sp = [int(x) for x in f]
# counter = 0
#
# summsp = 0
# for x in sp:
#     if x % 2 != 0:
#         summsp +=x
#         counter +=1
#
#
# arif = summsp//counter
# print(arif, 'arif')
# cnt = 0
# maxx = []
# for i in range(len(sp) - 2):
#     p1 = oct(sp[i] + sp[i+1])[2:]
#     p2 = oct(sp[i] + sp[i+2])[2:]
#     p3 = oct(sp[i+1] + sp[i+2])[2:]
#     summ = sp[i] + sp[i+1] + sp[i+2]
#     q1 = '7' not in str(p1) and '7' not in str(p2) and '7' not in str(p3)
#     q2 = summ < arif
#     if q1 + q2 == 2:
#         cnt+=1
#         maxx.append(sp[i] + sp[i+1] + sp[i+2])
#
# #
# print(cnt, max(maxx)) #25 5750
#

#
# with open('17-303.txt') as f:
#     sp = [int(x) for x in f]
# sp3 = []
# for i in range(100):
#     sp3.append(i**3)
#
# spmax = []
# for i in range(len(sp)):
#     if sp[i] in sp3:
#         spmax.append(sp[i])
#     print(sp[i])
# Max = max(spmax)
# print(Max)
# cnt = 0
# res = []
# for i in range(len(sp) - 2):
#     p1 = abs((Max - (sp[i] + sp[i +1] + sp[i + 2])))
#     q1 = (p1**0.5) == int(p1**0.5)
#     q2 = (p1**0.5) % 2 == 0
#     if q1 + q2 == 2:
#         cnt+=1
#         res.append([sum(sp[i:i+3]), sorted(sp[i:i+3])])
# print(res, '\n')
# print(cnt, max(res), '\n')
# print(3525 * 8520)


# sp = [int(x) for x in open('17-288.txt')]
# def sem(n):
#     r = ''
#     while n!=0:
#         r += str(n % 7)
#         n = n//7
#     return r[::-1]
#
# maxx = -float('inf')
# minn = []
# c = 0
# cout = 0
# cnt = 0
# for i in range(len(sp) - 3):
#     p1 = abs(sp[i]) % 10 == 3
#     p2 = abs(sp[i + 1]) % 10 == 3
#     p3 = abs(sp[i + 2]) % 10 == 3
#     p4 = abs(sp[i + 3]) % 10 == 3
#
#     q1 = int(sem(abs(sp[i]))[-1:] != '3')
#     q2 = int(sem(abs(sp[i + 1]))[-1:] != '3')
#     q3 = int(sem(abs(sp[i + 2]))[-1:] != '3')
#     q4 = int(sem(abs(sp[i + 3]))[-1:] != '3')
#     res = [sp[i], sp[i + 1], sp[i + 2], sp[i + 3]]
#     minn.append(max(res) - min(res))
#     #print(p1 + p2 + p3 + p4, "  P")
#     if (p1 + p2 + p3 + p4 >= 1) and ( q1 + q2 + q3 + q4 == 4):
#         cout +=1
# print(cout, min(minn))
# print(cout, ' cout')
# print(cnt, " cnt")
# print(c, "c")
#
#

# sp = [int(x) for x in open("17-316.txt")]
#
# def f(a, b):
#     str_a = str(a)
#     str_b = str(b)
#     if len(str_a) != len(str_b):
#         return 0
#     diff_count = False
#     for i in range(len(str_a)):
#         if str_a[i] != str_b[i]:
#             diff_count += 1
#     return diff_count == 2
#
# minn = min(sp[0], sp[len(sp) - 1])
# cnt = 0
# maxx = []
# for i in range(len(sp) - 2):
#     p1 = f(sp[i], sp[i + 1])
#     p2 = f(sp[i +1], sp[i + 2])
#     p3 = f(sp[i], sp[i + 2])
#     sum = sp[i] + sp[i +  1] + sp[i + 2]
#     if p1 + p2 + p3 >= 1 and sum > minn:
#         cnt += 1
#         maxx.append(sum)
# print(cnt, max(maxx))
# #3098 29764

# sp = [int(x) for x in open('../17_8504.txt')]
#
# cnt = 0
# maxx = []
# minn = min([x for x in sp if x % 10 == 5 and len(str(x)) == 3])
# for i in range(len(sp) - 1):
#     p1 = len(str(sp[i])) == 3
#     p2 = len(str(sp[i + 1])) == 3
#
#     q1 = (sp[i] + sp[i+1]) % minn == 0
#     if(p1 + p2) >=1 and q1 == True:
#         cnt +=1
#         maxx.append(sp[i] + sp[i+1])
#
# print(cnt, max(maxx))

sp = [int(x) for x in open('17.txt')]

maxx = max([m for m in sp if m % 1000 == 321])
cnt = 0
mmax = []
for i in range(len(sp) - 2):
    p1 = len(str(sp[i])) == 5
    p2 = len(str(sp[i + 1])) == 5
    p3 = len(str(sp[i + 2])) == 5

    q1 = sp[i] % 5 == 0
    q2 = sp[i + 1] % 5 == 0
    q3 = sp[i + 2] % 5 == 0
    summ = sp[i] + sp[i+1] + sp[i + 2]
    if (p1 + p2 + p3 == 2) and (q1 + q2 + q3 >= 1) and summ > maxx:
        cnt +=1
        mmax.append(summ)

print(cnt, max(mmax))

# sp = [int(x) for x in open('17MCKO.txt')]
# sp1 = sorted(set(sp), reverse=True)
# trt = sp1[2]
# cnt = 0
# maxx = []
# for i in range(len(sp) - 2):
#     p1 = sp[i] % 2 == 0
#     p2 = sp[i+1] % 2 == 0
#     p3 = sp[i+2] % 2 == 0
#     summ = sp[i] + sp[i+1] + sp[i+2]
#
#     if (((p1 + p2 + p3) <= 2) and (summ <= trt)):
#         cnt +=1
#         maxx.append(summ)
#
# print(cnt, max(maxx))

sp = [int(x) for x in open('17КЕГЭ.txt')]

maxchet = max([x for x in sp if x % 2 == 0])
maxnechet = max([x for x in sp if x % 2 != 0])
minn = []
cnt = 0

# if maxchet > maxnechet:
#     for i in range(len(sp)):
#         if sp[i]%2 == 0:
#             cnt +=1
#             minn.append(sp[i])
# else:
#     for i in range(len(sp)):
#         if sp[i] % 2 != 0:
#             cnt+=1
#             minn.append(sp[i])

for i in range(len(sp)):
         if sp[i]%2 == 0:
             cnt +=1
             minn.append(sp[i])
print(cnt, min(minn))