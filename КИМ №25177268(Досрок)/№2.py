from itertools import *

def f(x,y,z,w):
    return ((w==z) or (not(y <= w)) or (not(x)))

for a1, a2, a3, a4, a5 in product([0,1], repeat = 5):
    t = [(0,0,1, a1), (a2, 1,1, a3), (0,a4,a5,0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
                print(*p, sep = '')