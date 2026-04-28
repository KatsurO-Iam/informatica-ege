from itertools import *

s = '457 346 24 123 167 257 156'.split()
v = 'АВ АБ БВ БД ВЕ ДГ ДК ГК ГЕ ЕК'.split()
print(*range(1,8))
for p in permutations('АБВГДЕК'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)