from itertools import *

s = "367 346 1124 237 67 125 145".split()
v = 'AD AF DG GC DE GE CB EB BF'.split()

print(*range(1,8))
for p in permutations("ABCDEFG"):
    if all(str(p.index(b) + 1) in s[p.index(a)] for a,b in v):
        print(*p)