from itertools import *
def f(x,y,z,w):
    return ((x == (not y)) <= ((x and w) == (z and (not w))))

for a1, a2, a3, a4, a5, a6 in product([0,1], repeat=6):
    table = [(1,1,a1,1), (a2,1,1,a3), (0, a4,a5,a6)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(*dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p, sep='')

print('w x y z')
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                if ((x == (not y)) <= ((x and w) == (z and (not w)))) == 0:
                    print( w, x, y, z)