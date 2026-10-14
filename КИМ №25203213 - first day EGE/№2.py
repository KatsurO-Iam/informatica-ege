from itertools import *

def f(x,y,z,w):
    return (((w == (not(x))) <= (not(z <= w))) or (not(y)))

for a1,a2,a3,a4,a5 in product([0,1], repeat = 5):
    t = [(a1,0,1,0), (0,a2,a3,0), (a4,1,1,a5)]
    if len(set(t)) == len(t):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
                print(*p, sep = '')