from itertools import *
sp = list(product('айкле', repeat=5))
c = 0
i = 0
for x in sp:
    i+=1
    s = ''.join(x)
    if s.count('к') <= 1 and 'ее' not in s:
        print(i)
