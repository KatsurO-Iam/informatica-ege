from itertools import *

s = '56 378 26 68 17 134 258 247'.split()
v = 'AC AG AB BC BE CF ED FD GH HD'.split()
print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)
