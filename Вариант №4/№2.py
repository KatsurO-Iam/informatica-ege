from itertools import product,permutations

def f(x,y,z,w):
    return ((not((((not y) == w) and (z <= x)) <= y)))

for a1, a2, a3, a4, a5, a6, a7 in product([0,1], repeat=7):
    table = [(0, a1, a2, 0), (a3, 0, a4, 1), (a5, 1, a6, a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in table] == [1,1,1]:
                print(*p, sep = '')

#yzwx