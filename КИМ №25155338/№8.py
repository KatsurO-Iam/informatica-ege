from itertools import *
sp = list(product('0123456', repeat=6))
k = 0
for x in sp:
    x = ''.join(x)
    if x[0] != '0' and x[-1] != '0' and x[-1]!= '1' and [-1] !='2' and x[-1] != '3' and x[-1] != '4':
        x = x.replace('0', '*')
        x = x.replace('2', '*')
        x = x.replace('4', '*')
        x = x.replace('6', '*')

        x = x.replace('1', '@')
        x = x.replace('3', '@')
        x = x.replace('5', '@')

        if x.count('@') == x.count('*'):
            k+=1
print(k)