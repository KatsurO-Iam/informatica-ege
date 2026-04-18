from math import factorial
from itertools import *

c = 0
sp = list(product('мечта', repeat=6))
for x in sp:
    x = ''.join(x)
    if x.count('а') >= 3:
        c +=1
print(c)