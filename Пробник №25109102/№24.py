from re import*
sp = open('24.txt').readline()
alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
maxx = 0
maxx_ch = ''
for s in alph:
    if sp.count('X' + s) > maxx:
        maxx = sp.count('X' + s)
        maxx_ch = s
print(maxx_ch, maxx, sep='')
