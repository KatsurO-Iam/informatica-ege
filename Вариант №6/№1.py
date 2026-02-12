from itertools import *

v = '245 137 256 156 134 347 26'.split()
s = 'AG AB AC BC BD CE DE DF EG FG'.split()

print(*range(1,8))
for p in permutations('ABCDEFG'):
    if all(str(p.index(b)+1) in v[p.index(a)] for a,b in s):
        print(*p)