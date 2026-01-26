from itertools import *
sp = list(product('01234567', repeat=5))
c = 0
for x in sp:
    s = ''.join(x)
    if s[0] != '0' and s.count('2') == 2 and '22' not in s:
        c += 1

print(c)
