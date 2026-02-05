from itertools import *

s = '238 156 1 78 278 27 456 145'.split()
v = 'HE EB EG GD BD DC BA AC CF GF'.split()
print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
        print(*p)
#34
