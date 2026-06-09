from itertools import *

s = '258 17 56 68 138 347 26 145'.split()
v = 'DA DH HB HF FE GE GA GC AC BC'.split()
print(*range(1,9))

for p in permutations('ABCDEFGH'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
        print(*p)