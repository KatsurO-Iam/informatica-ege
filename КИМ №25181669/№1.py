from itertools import *

s = '458 37 26 178 168 357 246 145'.split()
v = 'AB AE BF EF EC FG CD DG CH DH GH'.split()
print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)
print(20+12)