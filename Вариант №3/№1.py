from itertools import *

s = '378 37 126 78 6 358 124 146'.split()
v = 'AC AB BD BE CD CF FG DG GE EH'.split()

print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)
#21