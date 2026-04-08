from itertools import *
sp = list(product('аекнот', repeat=7))
k = 0
for x in sp:
    k+=1
    x = ''.join(x)
    if k % 2 != 0 and ('а' not in x) and x.count('о') == 2 and x.count('к') == 2 and x.count('е') == 1 and x.count('т') == 1 and x.count('н') == 1:
        print(k ,x)
