from itertools import *
c = 0
sp = list(product('0123456', repeat = 6))
for x in sp:
    s = ''.join(x)
    if s[0] != '0' and s.count('0') == 1:
        s = s.replace('2', '*')
        s = s.replace('4', '*')
        s = s.replace('6', '*')
        if '*0' not in s and '0*' not in s and '*0*' not in s:
            c +=1
print(c)