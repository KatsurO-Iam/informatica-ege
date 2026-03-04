from itertools import *

s = '78 3568 246 37 28 23 14 125'.split()
v = 'AB BC BD BH AH DC HG DE GF EF'.split()
print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)
