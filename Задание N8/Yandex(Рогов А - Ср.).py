import itertools as t

sp = list(t.product('веностчь', repeat = 6))
cnt = 0
i = 0
for el in sp:
    i+=1
    if i % 2 == 0 and el.count('о') >= 2 and (el[0] == 'е' or el[0] == 'о'):
        cnt += 1
print(cnt)
#print(sp, sep='\n')  el[0] != 'в' or el[0] != 'н' or el[0] != 'с' or el[0] != 'т' or el[0] != 'ч' or el[0] != 'ь'