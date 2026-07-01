from itertools import *

sp = list(product('АЕЛНПР', repeat=6))

i = 0
for x in sp:
    i +=1
    x = "".join(x)
    if i % 2 != 0 and x.count('П') == 0 and x.count('Р') == 0 and x.count('А') == 2 and x.count('Н') == 1:
        print(x, i)