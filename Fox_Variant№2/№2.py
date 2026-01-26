from itertools import *

def f(x, y, z,w):
    return (((z==x) <= (w and z)) <= (((not y) and z) <= y))

for a1, a2 in product([0,1], repeat = 2):
    table = [(1,a1,0,0), (1,a2,0,1), (1,1,0,1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p, sep = '')