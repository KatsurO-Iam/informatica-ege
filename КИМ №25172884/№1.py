from itertools import *

s = '457 467 46 1236 17 2347 1256'.split()
v = 'АБ АВ АГ АЕ БВ ВГ ГЕ ВД ДЕ ЕЖ ДЖ'.split()
print(*range(1,8))
for p in permutations('АБВГДЕЖ'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)