from itertools import product, repeat

sp = list(product('аекнтц', repeat = 5))
c = 0
for x in sp:
    c +=1
    x = ''.join(x)
    if c % 2 == 0 and x[0] != 'а' and x[0] != 'е'  and x[0] != 'к' and x.count('ц') >= 2:
        print(c)
        break