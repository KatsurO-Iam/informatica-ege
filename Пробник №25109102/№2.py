# from itertools import *
# def f(x,y,z,w):
#     return (w or (x <= y) and ((not z) <= x))
#
# table = [(0,0,0,1), (0,0,1,0), (0,1,0,1)]
# if len(table) == len(set(table)):
#     for p in permutations('xyzw'):
#         if [f(*dict(zip(p, r))) for r in table] == [0, 0, 0]:
#             print(*p, sep='')
print('w z y x')
for w in 0,1:
    for z in 0,1:
        for x in 0,1:
            for y in 0,1:
                if (w or (x <= y) and ((not z) <= x)) == 0:
                    print(w, z, y, x)