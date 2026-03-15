from itertools import *

s = '248 168 568 157 347 237 456 123'.split()
v = 'AB AG AC BD BH HF HG GF CD CE DE EF'.split()

print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)
