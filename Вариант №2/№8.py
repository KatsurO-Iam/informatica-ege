from itertools import product

sp = list(product('аелрст', repeat=5))
i = 0
for s in sp:
    i +=1
    s = ''.join(s)
    if i % 2 != 0 and s[0] != 'а' and s[0] != 'с' and s[0] != 'т' and s.count('е') == 2 and 'ее' not in s:
        print(i, s)