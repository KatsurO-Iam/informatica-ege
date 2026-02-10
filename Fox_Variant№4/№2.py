from itertools import *

def f(x, y, z,w):
    return (x or ((not z) and y) or ( not(w <= y)))

for a1, a2,a3,a4,a5,a6,a7 in product([0,1], repeat = 7):
    table = [(1,0,a1,a2), (0,a3,1,a4), (a5,1,a6,a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p, sep = '')