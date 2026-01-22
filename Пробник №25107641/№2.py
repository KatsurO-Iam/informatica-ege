def f(x, y, z, w):
    return (not(z <= x ) or (y == w) or w)

from itertools import *
for a1,a2, a3, a4, a5, a6 in product([0,1], repeat=6):
    table = [(0,0, a1, a2), (0, a3, a4, a5), (0, 1, a6, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0,0,0]:
                print(*p, sep = '')
                