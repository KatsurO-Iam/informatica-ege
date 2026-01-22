from string import ascii_lowercase, digits
from itertools import *
alph = (digits + ascii_lowercase)[:15]
sp = list(product(alph, repeat=4))
k = 0
for x in sp:
    x = ''.join(x)
    if x[0] != '0' and x.count('8') == 1 and \
                all(n + n not in x for n in alph):
        k +=1
print(k)
#9295