
# z∨((w∨¬y)≡(x→z)),
def f(x,y,z,w):
    return ((w==y) or (((not x) <= z) and ((not z) <= y)))

from itertools import *
for a1, a2, a3, a4, a5,a6, a7,a8 in product([0,1], repeat = 8):
    table = [(a1, 1, 1, a2), (a3, a4, 1, a5),(1, a6,a7,a8)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0,0,0]:
                print(*p, sep = '')
# print('z y x w')
# k = 0
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 if (((not x)<=z)and(w or (not y))and (not z)) == 1:
#                     print(z,y,x,w)