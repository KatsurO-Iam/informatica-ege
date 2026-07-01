from itertools import permutations, product, repeat


def f(x,y,z,w):
    return ((not(z <= x)) or (y <= w) or (not(y)))

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat = 7):
    t = [(0,1,a1,a2), (a3,0,a4,a5), (1,a6,0,a7)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t))) for t in t] == [0,0,0]:
                print(*p, sep = '')