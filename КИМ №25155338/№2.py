from itertools import *

def f(a,b,c):
    return (a and (not b) or c)


table = [(0,0,0),(0,0,1),(0,1,0), (0,1,1), (1,0,0),(1,0,1), (1,1,0), (1,1,1)]
if len(table) == len(set(table)):
    for p in permutations('abc'):
        if [f(**dict(zip(p, r))) for r in table] == [0,1,1,1,0,0,1,1]:
            print(*p, sep = '')