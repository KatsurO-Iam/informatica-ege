from itertools import *

def f(x,y,z):
    """and/=="""
    return ((x == (not y)) or ((not x) and z))

for a1, a2, a3, a4, a5, a6 in product([0,1], repeat=6):
    table = [(0, a1, a2),
             (a3, 0, a4),
             (a5, a6, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyz'):
            if [f(**dict(zip(p, r))) for r in table] == [0,1,0]:
                print(*p, sep = '')