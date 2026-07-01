from itertools import *

sp = list(product('ВЕКОТЦ', repeat=6))

i = 0
c = 0
for x in sp:
    i +=1
    x = ''.join(x)
    if i % 2 != 0 and x.count('В') == 0 and x.count('Е') == 0 and x.count('К') == 0 and x.count('Т') == 2 and x.count('Ц') == 1:
        print(i)
        c+=1
print(c)