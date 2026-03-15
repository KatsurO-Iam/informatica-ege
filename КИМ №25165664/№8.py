from itertools import *
sp = list(permutations('логорифм', r=5))
k = 0
for x in sp:
    x = ''.join(x)
    for a in 'лгрфм':
        x = x.replace(a, '*')
    x = x.replace('о', '#')
    x = x.replace('и', '#')
    if '##' not in x and '**' not in x:
        k += 1
print(k)