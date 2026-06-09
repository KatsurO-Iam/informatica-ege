from itertools import product

s = list(product('акорст', repeat=5))

i = 0
for x in s:
    i+=1
    x = ''.join(x)
    if i % 2 == 0 and x[0] != 'а' and x[0] != 'с' and x[0] != 'т' and x.count('о')==2:
        print(i)