from itertools import *

s = '24567 146 5 12 1367 125 15'.split()
v = 'АВ ВБ ВЕ ВГ БГ ГД ГЖ ГЕ ДЖ ЕЖ'.split()
print(*range(1,8))
for p in permutations('АБВГДЕЖ'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)