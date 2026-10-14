from itertools import *

s = '47 35 246 136 267 345 15'.split()
v = 'DF DG GC CF FA CA AE GB BE'.split()
print(*range(1,8))

for p in permutations('ABCDEFG'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
        print(*p)
