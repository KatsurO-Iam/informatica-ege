from re import*
sp = open('24.txt').readline()
alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
maxx = -float('inf')
maxx_ch = ''
for s in alph:
    if sp.count('Q' + s) > maxx:
        maxx = sp.count('Q' + s)
        maxx_ch = s
print(maxx_ch, maxx, sep='')
