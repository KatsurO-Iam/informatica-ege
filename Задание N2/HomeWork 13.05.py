def f(x,y,z,w):
    return (w or (x <= y) and ((not z) <= x))

from itertools import *
table = [(0,0,0),(0,0,1),(0,1,0),(1,0,1)]
if len(table) == len(set(table)):
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0, 0]:
            print(*p, sep='')



# print('acdb')
# k = 0
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             for d in 0,1:
#                 if ((a <= b) and (b <= c) and (c <= d)) == 1:
#                     print(a,b,c,d)