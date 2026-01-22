from itertools import *

s = list(product('адуч', repeat = 5))
sp = []
for x in s:
    x = ''.join(x)
    if x[0] in 'ау':
        sp.append(x)
i = 0
for i in range(len(sp)):
    if sp[i] == 'удача':
        print(i+1)
