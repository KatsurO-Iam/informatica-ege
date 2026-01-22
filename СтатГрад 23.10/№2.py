# 1 - 105
# 2 - xywz
# 3 - 420
# 4 - 19
# 6 - 101084
# 7 - 405106
# 10 - 74
# 11 - 32768
# 12 - 604
# 18 - 6653 2522
# 22 - 103

from itertools import *

def f(x,y,z,w):
    return (((not x) and z and (not y) and (not w) or ((not x) and z and y and (not w)) or ((not x) and z and y and w)))

for a1, a2, a3, a4, a5, a6, a7 in product([0,1], repeat=7):
    table = [(a1, 1, 0, a2), (0,0,a3,a4), (a5,a6,1,a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in table] == [1,1,1]:
                print(*p, sep='')
