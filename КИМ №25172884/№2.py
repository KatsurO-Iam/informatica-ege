from itertools import *

def f(x,y,z,w):
    return ((x <= y) and ((not y) <= z) and w)

for a1, a2, a3, a4, a5, a6 in product([0,1], repeat=6):
    table = [
            (a1, a2, 0, 0),
            (0, 1, 0, a3),
            (0, a4, a5, a6)
             ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1,1,1]:
                print(*p, sep = '')