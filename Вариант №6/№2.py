# 1 - 24
from itertools import product,permutations


def f(x,y,z,w):
    return ((y <= z) and (w ==(x <= y)) and (not x))

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
    table = [(0,1,a1,a2), (1,a3,a4,a5), (a6,0,1,a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in table] == [1,1,1]:
                print(*p, sep = '')