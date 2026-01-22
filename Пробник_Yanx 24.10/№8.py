from itertools import *
c = 0
sp = list(permutations('артём', r = 5))
for x in sp:
    p1 = x[0] in 'аё'
    p2 = x[-1] in 'аё'
    if p1 + p2 == 1:
        c+=1
    elif p1 + p2 == 0:
        c += 1

print(c)