from itertools import product

alp = sorted('рябина')
i = 0
for x in product(alp, repeat=6):
    i +=1
    x = ''.join(x)
    if i % 2 == 0 and x[0] != 'н' and x[0] != 'р' and x[0] != 'я' and x.count('б') >= 1:
        print(x, i)