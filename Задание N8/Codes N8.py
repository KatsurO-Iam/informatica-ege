from itertools import *

# sp = list(t.permutations('апельсин', r = 7))
# cnt = 0
# i = 0
# for el in sp:
#     i+=1
#     if i % 2 == 0 and el.count('о') >= 2 and (el[0] == 'е' or el[0] == 'о'):
#         cnt += 1
# print(cnt)
# #print(sp, sep='\n')  el[0] != 'в' or el[0] != 'н' or el[0] != 'с' or el[0] != 'т' or el[0] != 'ч' or el[0] != 'ь'
c = 0
sp = list(permutations('артём', r = 5))
for x in sp:
    p1 = x[0] in 'аё'
    p2 = x[-1] in 'аё'
    if p1 + p2 == 1:
        c+=1
    elif p1 + p2 == 0:
        c += 1

print(c)