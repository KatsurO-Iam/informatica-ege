from itertools import *

def f(x,y,z):
    return ((x<=y) and (y<=z))

t = [(1,0,0),(1,0,1)]
for p in permutations('xyz'):
    if [f(**dict(zip(p,r))) for r in t] == [1,1]:
        print(*p, sep = '')