from itertools import *
sp = list(product('питоняга', repeat = 8))
cnt = 0
ss = []
for x in sp:
    x = ''.join(x)
    ss.append(x)

for x in ss:
    if x[0] not in 'иояа':
        if 'аа' not in x and 'оо' not in x and "яя" not in x and 'ии' not in x:
            cnt +=1

print(cnt)