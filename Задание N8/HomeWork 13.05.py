from itertools import *

s = list(product('аекптч', repeat = 7))

sp = []
for x in s:
    x = ''.join(x)
    sp.append(x)

w1 = ''
w2 = ''
for i in range(len(sp)):
    if sp[i] == 'аптечка':
        w1 = i
    elif sp[i] == 'печатка':
        w2 = i

cnt = 0
for i in range(w1 + 1, w2):
    cnt+=1
print(cnt)