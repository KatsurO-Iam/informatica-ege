from itertools import *

s = '38 468 157 26 378 247 356 125'.split()
v = 'AB AF AC BD BC CG GF FH HD HE ED'.split()
print(*range(1,9))

for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)
