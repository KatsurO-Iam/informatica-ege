from itertools import *
c = 0
sp = list(product('авкмос', repeat = 6))
for x in sp:
    s = ''.join(x)
    c+=1
    if c % 2 != 0 and s[0] != 'а' and s[0] != 'в' and s[0] != 'к' and s.count('м') == 2:
        print(c)
#23347