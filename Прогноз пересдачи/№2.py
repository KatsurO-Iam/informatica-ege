from itertools import *


def f(x,y,z,w):
    return ((not(z<=w)) or (x==y) or x)

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat = 7):
    t = [(0,a1,a2,0), (1,0,a3,a4), (a5,1,a6,a7)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
                print(*p, sep = '')