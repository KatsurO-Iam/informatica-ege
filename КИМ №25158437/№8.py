from itertools import *
sp = list(product('леся#', repeat=5))
k = 0
for x in sp:
    x = ''.join(x)
    if x[0] != '#' and x[-1] != '#' and x.count('#') == 1:
        x = x.replace('е', '*')
        x = x.replace('я', '*')

        x = x.replace('л', '@')
        x = x.replace('с', '@')
        if '**' not in x and '@@' not in x :
            k+=1
            print(x)
print(k)